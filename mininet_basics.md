Mininet Basic Commands:
=========================


1. To check the mininet version 
-------------------------------

```
mn --version
```

2. To clean up the existing ovs bridges, namespaces,
----------------------------------------------------


Note: sometime we mistakenly closed the mininet shell, or mininet crashed. But the topology components will continue to exists. To clean such stuff, cleanup command is used.


```
mn -c
```

3. Our First Simple Topology  
------------------------------

![Alt text](imgs/topo1.png?raw=true "Simple Topology")


```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 192.168.100.0/24 --topo=single,4, 
```




References:
--------------

1. http://mininet.org/walkthrough/

