RYU Part2:
=========

In this part , we are going to start writing the sample RYU applications step by step.

Base Rule for beginners:
Please copy the example application file and modify as per your needs.

In this ryu exercises, i am going to use Openflow 1.3 Version, and use simple_switch_13.py as example program to start with.


# RYU Application overview:


## Step1 : Import the base classes / library

```
from ryu.base import app_manager

from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls

from ryu.ofproto import ofproto_v1_3

from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
```

**app_manager :**   main entry point for the application.

**set_ev_cls, ofp_event, Dispatcher :**   used for capturing openflow event, when the openflow packet received

**ofproto_v1_3 :** Specifies which Openflow version to be used.

**packet, ethernet, ether_types :**  packet processing library



## step2:  Define your application class (derived from app_manager) and write the base stuff:

1.
```
class SimpleSwitch13(app_manager.RyuApp):
```
2.
sets the openflow version

```
 OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
```
3. define the constructor .
```
def __init__(self, *args, **kwargs):
super(SimpleSwitch13, self).__init__(*args, **kwargs)
```

## step3:  Handle the relavent Openflow events (when the openflow feature request message received, When the openflow packet in message received):

In the Event handler, write your application logic. 



# How to Implement Openflow L2 Switch in RYU :

1. mac_to_port dictionary to store the mac table.

2. In Switch Feature Request Event handler Insert table miss entry (using add_flow function).
   Table Miss entry flow:  Match all packets, priority 0, forward it to controller port.

3. In Packet_In Handler,
   Inspect the incoming packet,
      Update the mac_to_port dictionary wth "soruce mac" and " incoming port"
      Check the destination mac is present in the mac_to_port dictionary. 
      if present,
          match = inport, srcmac, dstmac
          action = forward ot the port number
          Add a flow (with match, action).
      else
           action = flood a packet
      call packet out with action. 


# Execute the Openflow L2 Switch :

```
ryu-manager simple_switch_13.py
```

Run the Mininet Topology
```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=linear,4
```

Check the output.



# References

https://en.wikipedia.org/wiki/OpenFlow

http://ryu.readthedocs.io/en/latest/

https://osrg.github.io/ryu/resources.html

https://github.com/osrg/ryu/tree/master/ryu
