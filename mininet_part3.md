# Writing Custom Topology in Mininet

This tutorial helps to learn on writing mininet custom topology.

## Introduction

mininet exposes the python API. We can create a custom topologies using the python API with few lines of code.  


## How to write Custom Topology in Mininet
 
Steps are below.


### 1. Import the python required libraries

 ``` 
from mininet.topo import Topo
from mininet.net import Mininet
 ``` 

### 2. Write the Topology definition class

 ``` 
 class CustomTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        self.addLink(h1, s1)
        self.addLink(h2, s2)

 ``` 

Important Topology definition APIs:

a. addSwitch, 

b. addHost, 

c. addLink



### 3. Start the Topology


a. Create the Topology object

b. Create the Mininet with Topology object

c. Start the Mininet


``` 
if __name__ == '__main__':
    topo = SingleSwitchTopo()
    net = Mininet(topo)
    net.start()
``` 


## References:

1. https://github.com/mininet/mininet/wiki/Introduction-to-Mininet

2. https://github.com/mininet/mininet/tree/master/examples

3. http://mininet.org/api/annotated.html

# To read
4. https://kiranvemuri.info/dynamic-topology-changes-in-mininet-advanced-users-5c452f7f302a

4. https://stackoverflow.com/questions/43070043/mininet-wifi-custom-topology
https://stackoverflow.com/questions/43070043/mininet-wifi-custom-topology