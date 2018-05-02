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



# Objective:

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



# References:


1. openflow 1.3 specification documemnt, 5.6 Group table


2. https://www.quora.com/Why-dose-the-Openflow-protocol-exist-the-group-table-And-what-the-relationship-between-pipeline-and-group-table


3. http://www.muzixing.com/pages/2014/11/07/load-balancemultipath-application-on-ryu.html

4. https://github.com/muzixing/ryu/tree/master/ryu/app/multipath
