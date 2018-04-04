# mininet-custom topologies

## Example1

In the example1, we creates a Linear Topology with two hosts and two switches with local controller and runs the pingall command and exits it.


Run the RYU app

```
ryu-manager ryu.app.simple_switch_13
```


Run the Mininet Custome Topology file

```
python example1.py
```




## Example2

In the example2, we creates a Linear Topology 
1. Two hosts and two switches. 
2. Assigns the custom MAC Address, IP address for each Host.
3. Using external controller
4. start the CLI Prompt


Run the RYU app

```
ryu-manager ryu.app.simple_switch_13
```


Run the Mininet Custome Topology file

```
python example2.py
```



## Example3

In the example3, we creates a RING Topology 
1. Four hosts and Four switches
2. Switches are connected in RING model. 
2. Assigns the custom MAC Address, IP address for each Host.
3. Using external controller
4. start the CLI Prompt

Note: We must use SDN STP application. 


Run the RYU app

```
ryu-manager ryu.app.simple_switch_stp
```


Run the Mininet Custome Topology file

```
python example1.py
```


## Example4

In the example4, we creates a Linear Topology  and runs IPERF TCP Test between the hosts
1. Two hosts and two switches. 
2. Assigns the custom MAC Address, IP address for each Host.
3. Using external controller
4. Run the iperf server command in the h1 host
5. Run the iperf client command in the h2 host
6. Start the CLI Prompt




Run the RYU app

```
ryu-manager ryu.app.simple_switch_13
```


Run the Mininet Custome Topology file

```
python example4.py
```



Further References:

https://github.com/panandr/mininet-fattree
https://github.com/clement10601/FatreeMinineTopo/blob/master/topo.py
https://github.com/narendran/mininet-topos
https://github.com/palakbhonsle/Mininet
https://github.com/yoshizaki/mininet

https://github.com/hdb3/mininetquagga