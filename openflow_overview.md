# How Traditional L2 Switch Works (Technical details) :

1. Traditional Switch have built in Control Plane + Data Plane.
2. Mac Table( a.k.a Forwarding table) is Empty when the switch starts.
3. Control Plane updates the Mac Table with the MAC and the PORT Number. This information is extracted from incoming Packet.
4. Control Plane keeps on building/updating the Mac Table.
5. When the packet arrives, Switch Data plane looks the Mac table, if the destination MAC matches in the Mac table, it forwards the packet to the respective Port.


# How SDN Switch(Openflow Switch) Works:


1. RYU L3 Application

```
ryu-manager ryu.app.simple_switch_13
```


2. Run the Linear Mininet Topology, 

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=linear,4
```


3. Start Wireshark Capture


## overview

1. Switch is configured with SDN Controller IP and Openflow protocol version.
2. Switch will establish the communication with SDN Controller.
3. Initialy the Switch flow table will be empty, When the Packet arrives Switch will send the packets to the Controller.
4. Controller build the Switch Logic with the packets.
5. Controller adds the Flow table to the switch.
6. Now, Switch data path is built with flows. So when the Packet arrive it will look the Flow table and forward the packet to respective port.



# Openflow Messages in Detail:


## 1.Hello Message:

   a.  Switch sends Openflow Hello Message(includes version number) to the Controller (port number 6653)

   b.  Controller responds with the Hello Message if version is supported.

  Failure Case(Version MisMatch):

   If different Openflow Version is user between the Controller and Switch, Hello Message will fail.
   
   You will see similar error msg in the controller.

  	Error:
  	unsupported version 0x1. If possible, set the switch to use one of the versions [3]


## 2.Features Request/Reply Message:

  a. Controller will send the Feature Request Message to the Switch and asking for the Switch supported features.

  b. Switch will reply with
     datapath ID, buffers, tables size,
     stats reporting : flow stats, port stats, table stats etc.


## 3.Port Desc/Status Message:
	
   a. Controller will ask for the port description/ status message.

   b. Switch will send the Port details of each port.


## 4. Packet In/Packet Out Message:

   a. If Switch want to send a data packet to the Controller, it uses the PACKET IN message
     
   b.Controller process the Packet in message, and decides what to do(which port to forward/ or drop etc) with this packet.
     
   c. Controller respond with Packet Out Message with actions (FLOOD etc.)

## 5. Flow Modification(add,delete) Message:
	
   a. To add, remove, modify the flow in the switch, controller using this message.

   b. Controller Sends the Flow Modification message to the switch with this important params.
	i). Command,
	ii). Match
	iii). Instruction, action.

	At the time of switch starts(initial negotiatian), Controller adds TABLE MISS entry in to the switch.
   ### Table Miss Entry:
 
 The flow entry that wildcards all fields (all fields omitted) and has priority equal to 0 is called the table-miss flow entry
 RYU installs the table miss entry to forward the packets to the controller port(action = output:Controller port).


## 6. Echo Request/Reply Message: 

   To identify the liveliness of the Controller, Switch will send periodic health Check message to the Controller and expects the response. (default: 5sec interval)

 A. Switch sends Echo Request to the Controller.

 B. Controller responds back with Echo Reply.


## 7. Stats Message:

   1. flow(individual,aggregate),table,port,queue stats message will send by the controller.

   2. Switch will respond with the relavent statistics.

   This is used for monitoring the switches (with variour counter packets/sec, errors, etc)


# Important Openvswitch Commands

```
sudo ovs-vsctl show
sudo ovs-ofctl -O <openflow-version> show <switch-name>
sudo ovs-ofctl -O OpenFlow13 show s1
sudo ovs-ofctl -O Openflow13 dump-flows s1
```


# Take aways:

1) Openflow version should match between the switch and Controller

2) Our Controller Application(our RYU project/exercise) should process Packet IN (Message), to build the Switching/Routing logic.

3) Our Controller Application(our RYU project/exercise) should use Flow Modifcation message to add/modify/delete the flows in the switch.

4) Our Controller Application(our RYU project/exercise) should use Flow Stats, Port Stats request message to get the statistics(Packets Sent/Received , etc) of the flows, Ports .



# References

https://www.opennetworking.org/software-defined-standards/specifications/

https://osrg.github.io/ryu/resources.html
