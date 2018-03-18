RYU Part6:
=========

In this exercise, We are going to include the flow priority  in  the simple_switch_13.py(Layer 2 Switch). 

In this exercise, we will add the TCP DROP flow( Match ALL Traffic) with higher priority. Remaining traffic will go via the L2 Switch flows.



*Flow Priority*

priority: matching precedence of the flow entry

size: 2 bytes

The packet is matched against flow entries in the flow table and only the highest priority flow entry that matches the packet must be selected





## High level Steps:

1. Add the ICMP Drop flow with priority 10000 in Openflow Feature Request event


## Code changes:

Copy the simple_switch_13.py to ex5_flow_priority.py file
```
cp simple_switch_13.py ex5_flow_priority.py
```
Modify the ex5_flow_priority.py file as below,


include the libs
```
from ryu.lib.packet import in_proto
from ryu.lib.packet import ipv4
```

In the switch_features_handler function, Add the TCP drop flow

Note: Default Action is DROP. 

```    
        match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP, ip_proto=in_proto.IPPROTO_TCP)
        mod = parser.OFPFlowMod(datapath=datapath, table_id=0, priority=10000, match=match)
        datapath.send_msg(mod)

```


## Test


Ryu Application

```
ryu-manager ex5_flow_priority.py
```

Mininet Topology

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=single,4   -x
```

Check the flows

```
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```

Lets Ping and watch the flows


Perform IPERF Test

h4 node
```
iperf -s
```
h1 node
```
iperf -c 10.1.1.4 -P 10
```


OVS flows
```
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```




# Reference:

1. https://www.opennetworking.org/software-defined-standards/specifications/

page 155 contains timeout details.

2. API details
http://ryu.readthedocs.io/en/latest/ofproto_v1_3_ref.html?highlight=OFPFlowMod
