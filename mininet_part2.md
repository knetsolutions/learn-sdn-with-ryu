# Mininet Commands:


## 1. TCP/UDP Traffic Tests


### a. Setup the Topology with xterms options (open terminal for each Node)

![Alt text](imgs/topo2.png?raw=true "Linear Topology")


```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=linear,4  -x
```

### a.  TCP Traffic Test between h1 to h4


Run IPERF TCP Server in h4

```
iperf -s

```


RUN IPERF TCP Client in h1


```
iperf -c 10.1.1.4 -i 10 -t 30
iperf -c 10.1.1.4 -i 10 -P 10 -t 30

```


### b.  UDP Traffic Test between h1 to h4


Run IPERF UDP Server in h4

```
iperf -s -u

```


RUN IPERF UDP Client in h1


```
iperf -c 10.1.1.4 -b 10m -i 10 -t 30
iperf -c 10.1.1.4 -b 10m -i 10 -P 10 -t 30

```




## 2. Torus Topology 

>Torus Topology is mesh interconnect with nodes arranged in a rectilinear array of N = 3, or more dimensions
>3,3 =   3 Rows and 3 columns (Matrix) of Nodes and Switches, and inter connected.

This topology forms a Loop.


```
sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=torus,3,3

```

References:
--------------

1. http://mininet.org/walkthrough/

2. https://en.wikipedia.org/wiki/Torus_interconnect

