RYU Part4:
=========

In this exercise, We are going to modify the simple_switch_13.py(Layer 2 Switch) application to Layer 4 Switch.

We will populate the flow tables based on Layer 4 information( source ip and destination ip, transport protocol(udp or tcp), src port and destinaton port).

## High level Steps:

1. In the ethernet packet, check the ether frame type field is IP.
2. if it is IP, load the IP Packet from the packet.
3. extract the srcip , and dst ip from IP Packet.
4. Check the IP Protocol 
5. If it is ICMP
   Prepare the openflow match with IP Src, IP dst and Protocol.
6. If it is TCP,
    extract the tcp src port  and tcp dst port fied
    Prepare the openflow match with IP Src, IP dst and Protocol, TCP Src Port and TCP dst port..
7. If it is UDP
	Extract the udp src port  and tcp dst port fied
    Prepare the openflow match  with IP src, IP dst , protcol, udp src and udp dst port.



## Code changes:

Copy the simple_switch_13.py to ex3_L4Match_switch.py file
```
cp simple_switch_13.py ex3_L4Match_switch.py
```

Modify the ex3_L4Match_switch.py file as below,

Include the required library modules
```
from ryu.lib.packet import in_proto
from ryu.lib.packet import ipv4
from ryu.lib.packet import icmp
from ryu.lib.packet import tcp
from ryu.lib.packet import udp
```

Populate the IP Match (replace the ethernet match)

```

            # check IP Protocol and create a match for IP
            if eth.ethertype == ether_types.ETH_TYPE_IP:
                ip = pkt.get_protocol(ipv4.ipv4)
                srcip = ip.src
                dstip = ip.dst
                protocol = ip.proto
            
                # if ICMP Protocol
                if protocol == in_proto.IPPROTO_ICMP:
                    match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP, ipv4_src=srcip, ipv4_dst=dstip, ip_proto=protocol)
            
                #  if TCP Protocol
                elif protocol == in_proto.IPPROTO_TCP:
                    t = pkt.get_protocol(tcp.tcp)
                    match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP, ipv4_src=srcip, ipv4_dst=dstip, ip_proto=protocol, tcp_src=t.src_port, tcp_dst=t.dst_port,)
            
                #  If UDP Protocol 
                elif protocol == in_proto.IPPROTO_UDP:
                    u = pkt.get_protocol(udp.udp)
                    match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP, ipv4_src=srcip, ipv4_dst=dstip, ip_proto=protocol, udp_src=u.src_port, udp_dst=u.dst_port,)            


```

## Test

We need to send TCP/UDP Traffic to see TCP/UDP Flows.


Ryu Application

```
ryu-manager ex3_L4Match_switch.py
```

Mininet Topology

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=linear,4  -x
```

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

page 62 contains match fields.

2. https://en.wikipedia.org/wiki/Ethernet_frame

3. https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers
