RYU Part3:
=========

In this exercise, We are going to modify the simple_switch_13.py(Layer 2 Switch) application to Layer 3 Switch.

We will populate the flow tables based on Layer 3 information( source ip and destination ip).

## High level Steps:

1. In the ethernet packet, check the ether frame type field is IP.
2. if it is IP, load the IP Packet from the packet.
3. extract the srcip , and dst ip from IP Packet.
4. Prepare the Openflow Match  with  eth_type, ipv4_src, ipv4_dst ertype


## Code changes:

Copy the simple_switch_13.py to ex2_L3Match_switch.py file

```
cp simple_switch_13.py ex2_L3Match_switch.py
```
Modify the ex2_L3Match_switch.py file as below,

Include the required
```
from ryu.lib.packet import ipv4
```

Populate the IP Match (replace the ethernet match)

```
    # check IP Protocol and create a match for IP
    if eth.ethertype == ether_types.ETH_TYPE_IP:
        ip = pkt.get_protocol(ipv4.ipv4)
        srcip = ip.src
        dstip = ip.dst
        match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP,
                                ipv4_src=srcip,
                                ipv4_dst=dstip
                                )
```


## Test:

Ryu Application

```
ryu-manager  ex2_L3Match_switch.py

```

Mininet Topology

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=linear,4 

```

Check the OVS flows


```
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```


# Reference:

1. https://www.opennetworking.org/software-defined-standards/specifications/

page 62 contains match fields.

2. https://en.wikipedia.org/wiki/Ethernet_frame
