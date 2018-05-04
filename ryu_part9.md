ARP Proxy example
===================

This exercise helps to understand, generating packets from the controller.
This is ARP Proxy application. This application answers the ARP requests(instead of forwarding the ARP broadcasts to all hosts)


## Objective

This Application act as ARP Proxy. It captures the ARP Packets, builds the ARP response and send it to the Src.


## code changes :

1. include the lib

```
from ryu.lib.packet import arp
```

2. define your table

```
arp_table = {"10.0.0.1": "00:00:00:00:00:01",
             "10.0.0.2": "00:00:00:00:00:02",
             "10.0.0.3": "00:00:00:00:00:03",
             "10.0.0.4": "00:00:00:00:00:04"
             }
```


3. Write your arp proxy function.


```
    def arp_process(self, datapath, eth, a, in_port):
        r = arp_table.get(a.dst_ip)
        if r:
            self.logger.info("Matched MAC %s ", r)
            arp_resp = packet.Packet()
            arp_resp.add_protocol(ethernet.ethernet(ethertype=eth.ethertype,
                                  dst=eth.src, src=r))
            arp_resp.add_protocol(arp.arp(opcode=arp.ARP_REPLY,
                                  src_mac=r, src_ip=a.dst_ip,
                                  dst_mac=a.src_mac,
                                  dst_ip=a.src_ip))

            arp_resp.serialize()
            actions = []
            actions.append(datapath.ofproto_parser.OFPActionOutput(in_port))
            parser = datapath.ofproto_parser  
            ofproto = datapath.ofproto
            out = parser.OFPPacketOut(datapath=datapath, buffer_id=ofproto.OFP_NO_BUFFER,
                                  in_port=ofproto.OFPP_CONTROLLER, actions=actions, data=arp_resp)
            datapath.send_msg(out)
            self.logger.info("Proxied ARP Response packet")
```


4. In the packet handler function, if it arp packet, call the arp_proxy function.

```
        # Check whether is it arp packet
        if eth.ethertype == ether_types.ETH_TYPE_ARP:
            self.logger.info("Received ARP Packet %s %s %s ", dpid, src, dst)
            a = pkt.get_protocol(arp.arp)
            self.arp_process(datapath, eth, a, in_port)
            return
```



## Testing

1. Run your topology ( Linear topology)

```
sudo mn --controller=remote,ip=127.0.0.1 --mac  --switch=ovsk,protocols=OpenFlow13 --topo=linear,4 
```

2. Run the RYU controller application


```
ryu-manager ex8_arp_proxy.py
```

3. run tcpdump in the nodes

In mininet

```
xterm h1
xterm h2
```
in the xterminal,
```
tcpdump -i any -v
```


4. ping host1 to host2 from the mininet

```
h1 ping h2
```

5. check the tcpdump output


# References:

https://github.com/osrg/ryu/blob/master/ryu/lib/packet/arp.py
