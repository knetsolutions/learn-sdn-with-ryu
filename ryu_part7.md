RYU Part7:
=========

In this exercise, We are going to update the simple_switch_13.py(Layer 2 Switch)with PIPELINE PROCESSING (multiple tables) . 


![Alt text](imgs/pipeline.png?raw=true "PipeLine Processing")

We will create two tables
FILTER TABLE(Table 5) and FORWARD TABLE(Table 10).

FILTER TABLE : will add  packet filter rules (ACL rules). Block ICMP traffic.

FORWARD TABLE:  Here, our forwarding rules (L2 switch)



## High level Steps:

In Switch Feature Event Handler, add the table creation/initialization stuff as below.

1. In Table 0(default), Add the Match all Flow with action GO TO - Filter Table.

2. In Table 5(Filter Table), Add the Match All Flow with the Action GO TO - Forward Table

3. In Table 10(Forward Table), Add the Table Miss Entry.

4. Apply the filter rules(Drop ICMP Traffic) in the filter table.


The Layer2 switching logic, will update the Flow rules in FORWARD Table.



## Code changes:


Library inclusion
```    
from ryu.lib.packet import ipv4
from ryu.lib.packet import in_proto

FILTER_TABLE = 5
FORWARD_TABLE = 10

```

Create the table initialization.

```
    def add_default_table(self, datapath):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionGotoTable(FILTER_TABLE)]
        mod = parser.OFPFlowMod(datapath=datapath, table_id=0, instructions=inst)
        datapath.send_msg(mod)

    def add_filter_table(self, datapath):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionGotoTable(FORWARD_TABLE)]
        mod = parser.OFPFlowMod(datapath=datapath, table_id=FILTER_TABLE, 
                                priority=1, instructions=inst)
        datapath.send_msg(mod)

    def apply_filter_table_rules(self, datapath):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP, ip_proto=in_proto.IPPROTO_ICMP)
        mod = parser.OFPFlowMod(datapath=datapath, table_id=FILTER_TABLE,
                                priority=10000, match=match)
        datapath.send_msg(mod)

```

This table intialization routine will be placed in the switch_features_handler routine.


In the add_flow function, we specify the tableid as FORWARD Table.



## Test


Ryu Application

```
ryu-manager ex6_multiple_tables.py
```

Mininet Topology

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=single,4   -x
```

Lets Ping and watch the flows


IPERF Test

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

page 16 contains pipeline details (multiple .

2. API details
http://ryu.readthedocs.io/en/latest/ofproto_v1_3_ref.html?highlight=OFPFlowMod
