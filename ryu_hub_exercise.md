RYU Exercise :  HUB  Implementation
===================================

## Hub:

When a packet arrives at one port, it is copied to the other ports so that all segments of the LAN can see all packets.


In this exercise, We are going to modify the simple_switch_13.py(Layer 2 Switch) application to Hub application.


## High level Steps:

In the switch feature handler, instead of table miss entry, intall the proactive flood(all ports) flow

1. Add the proactive flow with empty match(All packets will match) with action FLOOD to all ports. 




## Code changes:

Copy the simple_switch_13.py to hub.py file

```
cp simple_switch_13.py hub.py
```

Modify the hub.py file as below,



Populate the IP Match (replace the ethernet match)

```
        actions = [parser.OFPActionOutput(port=ofproto.OFPP_FLOOD)]

```


## Test:

Ryu Application

```
ryu-manager  hub.py

```

Mininet Topology

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=simple,4 

```

Check the OVS flows


```
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```

