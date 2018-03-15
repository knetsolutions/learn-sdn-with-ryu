Mininet Basic Commands:
=========================


## 1. To check the mininet version 


```
mn --version
```


## 2. To clean up the existing ovs bridges and namespaces


Note: sometime we mistakenly closed the mininet shell, or mininet crashed. But the topology components will continue to exists. To clean such stuff, cleanup command is used.


```
mn -c
```


## 3. Our First Topology (Single)  



Topology with Single Switch and 4 Nodes.

![Alt text](imgs/topo1.png?raw=true "Single Topology")

RYU SDN Controller 

```
ryu-manager ryu.app.simple_switch_13
```

Mininet Topology

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=single,4
```


|  options    |    Description                                                        |
|-------------|-----------------------------------------------------------------------|
|--controller | type of controller local/remote and remote controller ip.             |
|             |  																	  |
|--mac        | mac address starts with 00:00:00:00:00:01							  |
|             |																		  |
|-i           | IP Subnets for the Topology 										  |
|             |																		  |
|--switch     | Switch type (ovsk - openvswitch kernel module), and openflow version. |
|             |																		  |
|--topo       | topology type(linear,minimal,reversed,single,torus,tree) and params.  |



## 4. Mininet Basic Shell Commands



Informative commands

```
help
dump
net
links
```

Action commands
```
pingall
<node-name> <command> {args}
h1 ifconfig
h1 ping h2
h1 ip route
```

## 5. Linear Topology 

linear topology (where each switch has one host, and all switches connect in a line)


![Alt text](imgs/topo2.png?raw=true "Linear Topology")


```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=linear,4
```



## 6. Tree Topology 


![Alt text](imgs/topo3.png?raw=true "Tree Topology")

```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --topo=tree,depth=2,fanout=3

```


fanout : each switch is connected to these many childs
depth : depth of the tree



References:
--------------

1. http://mininet.org/walkthrough/

2. https://en.wikipedia.org/wiki/Torus_interconnect

