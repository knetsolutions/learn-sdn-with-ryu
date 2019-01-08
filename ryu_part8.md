RYU Part8 - Group Table
=========================


### What is group table?

The ability for a flow entry to point to a group enables OpenFlow
to represent additional methods of forwarding (e.g. select and all).

### Usecase1:

Copy the packet to ALL buckets and process it.  (Ex: Sniffer/Port Monitor)

![Alt text](imgs/group_table.png?raw=true "Group table example")


### Usecase2:

Forward the packet to 1 bucket(out of N buckets) and process it.  (Load Balancer)

![Alt text](imgs/group_table1.png?raw=true "Group table example")



# 1. Sniffer Demo


We wants to capture all the traffic travels via switch S1, in the sniffer host.


## Topology Diagram

![Alt text](imgs/group_table.png?raw=true "Group table example")

Topology file: mininet_topologies/group_table_topo.py

### Logic:

S1 has three ports. port1 connected to sniffer host, port2 connected to S2, Port3 connected to S3.

### Switching Logic to applied in S1 :

   1. The packets received from Port2 will be forwarded to Port3 and Port1
   2. The packets received from Port3 will be forwarded to Port2 and Port1 


How to achieve this,

### Group table1(Group Table ID 50):

Create a Group table with  TYPE=ALL(it means,  copy a packet for each bucket. and each bucket will be processed). create two buckets. one bucket will send the packet to Port3, another bucket will send the packet to Port1


### Group table2(Group ID 51):

Create a Group table with  TYPE=ALL(it means,  copy a packet for each bucket. and each bucket will be processed). create two buckets. one bucket will send the packet to Port2, another bucket will send the packet to Port1


Create a proactive flows in Switch S1:

1.  All the packets received from port2  will be forwarded to Group table1(Group table ID 50)

2.  All the packets received from port3  will be forwarded to Group table2(Group table ID 51)





## Code changes:


Creat a function for creating the group 

``` 
    def send_group_mod(self, datapath):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # Hardcoding the stuff, as we already know the topology diagram.
        # Group table1
        # Receiver port2, forward it to port1 and Port3

        actions1 = [parser.OFPActionOutput(1)]
        actions2 = [parser.OFPActionOutput(3)]
        buckets = [parser.OFPBucket(actions=actions1),
                   parser.OFPBucket(actions=actions2)]
        req = parser.OFPGroupMod(datapath, ofproto.OFPGC_ADD,
                                 ofproto.OFPGT_ALL, 50, buckets)
        datapath.send_msg(req)

        # Group table2
        # Receive Port3, forward it to port1 and Port2
        actions1 = [parser.OFPActionOutput(1)]
        actions2 = [parser.OFPActionOutput(2)]
        buckets = [parser.OFPBucket(actions=actions1),
                   parser.OFPBucket(actions=actions2)]
        req = parser.OFPGroupMod(datapath, ofproto.OFPGC_ADD,
                                 ofproto.OFPGT_ALL, 51, buckets)
        datapath.send_msg(req)
``` 


Add Proactive Flows for switch1 (in switch feature event)



```
        # switch s1
        if datapath.id == 1:
            # add group tables
            self.send_group_mod(datapath)
            actions = [parser.OFPActionGroup(group_id=50)]
            match = parser.OFPMatch(in_port=2)
            self.add_flow(datapath, 10, match, actions)
            # entry 2
            actions = [parser.OFPActionGroup(group_id=51)]
            match = parser.OFPMatch(in_port=3)
            self.add_flow(datapath, 10, match, actions)

```


## Testing:

1. start the RYU controller

```
ryu-manager ex7_group_tables.py
```

2. start the mininet topology

```
sudo python group_table_topo.py
```

3. verify the group tables and proactive flows in switch S1

```
sudo ovs-ofctl -O OpenFlow13 dump-groups s1
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```

4. pingll, and ping h1 to h6 continuously


5. capture the packets in sniffer host (tcpdump). we can see the ping packets in sniffer host.



# 2. Loadbalancer Demo


Note:  

**This is not the full fledged the Loadbalancer project, I just want to demonstrate the Group Table Load balancer functionality. Hence I hardcoded the topology information in the RYU load balancer application with proactive flows.**


## Topology Diagram

![Alt text](imgs/group_table1.png?raw=true "Group table example")

Topology file:  mininet_topologies/group_table_lb.py


##  Application Logic:


1. In the switch S1, and S4

   Add the group table 50 -  
   This group table is type OFPGT_SELECT with two buckets.
   Bucket1 - Output to Port1
   Bucket2 - Output to Port2 

   So , when the packet enters in this group table, it will select(switch implementation specific algorithm)  any one bucket and send this packet.


2. In Switch S1, When the packet enters from port 3, send it to group table 50.

3. In switch S1, when the packet enters from port 1 or 2, send it to port3.

4. In Switch S4, When the packet enters from port 3, send it to group table 50.

5. In switch S4, when the packet enters from port 1 or 2, send it to port3.

6. In Switch S2 and S3, it just need to forward the packet to other port. 

## Code overview:


ryu-exercises/load-balancer.py


## Testing:



1. start the RYU controller

```
ryu-manager load_balancer.py
```

2. start the mininet topology

```
sudo python group_table_lb.py
```

3. verify the group tables and proactive flows in switch S1,S4,S2,S3

```
sudo ovs-ofctl -O OpenFlow13 dump-groups s1
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
sudo ovs-ofctl -O OpenFlow13 dump-groups s4
sudo ovs-ofctl -O OpenFlow13 dump-flows s4
sudo ovs-ofctl -O OpenFlow13 dump-flows s2
sudo ovs-ofctl -O OpenFlow13 dump-flows s3
```

4. Add a arp entry: ??



5. Test the ping and verify the status of load balancing

```
sudo ovs-ofctl -O OpenFlow13 dump-group-stats s1
sudo ovs-ofctl -O OpenFlow13 dump-group-stats s4
sudo ovs-ofctl -O OpenFlow13 dump-flows s2
sudo ovs-ofctl -O OpenFlow13 dump-flows s3

```


6. Test the TCP Traffic between h1 and h2


```
mininet> h2 iperf  -s &
mininet> h1 iperf  -c h2 -t 30 
```

Check the stats

```
sudo ovs-ofctl -O OpenFlow13 dump-group-stats s1
sudo ovs-ofctl -O OpenFlow13 dump-group-stats s4
sudo ovs-ofctl -O OpenFlow13 dump-flows s2
sudo ovs-ofctl -O OpenFlow13 dump-flows s3

```


7. Openvswitch Group table implementation details

http://docs.openvswitch.org/en/latest/faq/openflow/

8. Test the TCP Traffic with parallel streams beween h1 and h2 and check the status

```
mininet> h2 iperf  -s &
mininet> h1 iperf  -c h2 -P 4 -t 30 
```

Check the stats

```
sudo ovs-ofctl -O OpenFlow13 dump-group-stats s1
sudo ovs-ofctl -O OpenFlow13 dump-group-stats s4
sudo ovs-ofctl -O OpenFlow13 dump-flows s2
sudo ovs-ofctl -O OpenFlow13 dump-flows s3

```

























# References:


1. openflow 1.3 specification documemnt, 5.6 Group table

2. http://ryu.readthedocs.io/en/latest/ofproto_v1_3_ref.html

3. https://www.quora.com/Why-dose-the-Openflow-protocol-exist-the-group-table-And-what-the-relationship-between-pipeline-and-group-table


4. http://www.muzixing.com/pages/2014/11/07/load-balancemultipath-application-on-ryu.html
