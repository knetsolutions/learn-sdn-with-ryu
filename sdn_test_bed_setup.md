How to setup SDN Test bed:
=========================


# OS:  Ubuntu 16.04.04 LTS

As first step, please run this command.

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git gcc python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev zlib1g-dev python-pip
```


At the time of writing, Ubuntu 16.04 official repository has the stable releases for the tools as,

```
Tool Name       Version
*************************
Openvswitch :     2.5.2 
Wireshark   :     2.2.6
IPERF       :     2.0.5
```

Mininet will be installed from the script, and RYU will be installed using PIP.

```
Tool Name      Version
*************************
Mininet   :     2.2.2
RYU       :     4.23
```


1.Openvswitch Installation
-----------------------

```
sudo apt-get install openvswitch-switch
```

*To verify :*

```
ovs-vsctl --version
```

2.Wireshark Installation
-------------------------


```
sudo apt-get install wireshark

```

*To verify :*

```
sudo wireshark &

```

3.IPERF installation
---------------------


```
sudo apt-get install iperf
```

*To verify :*


```
iperf --version

```

4.RYU installation
------------------


```
sudo pip install ryu

```

*To verify :*


```
ryu-manager --version

```

5.Mininet Installation
------------------------

The default mininet install option installs openvswitch, wireshark, pox, ryu, nox ,openflow reference implemenation, etc. we dont require all these packages now. 
So we specify the option(-n) to install only mininet.

```
git clone git://github.com/mininet/mininet
cd mininet
git tag
git checkout 2.2.2
cd ..
mininet/util/install.sh --help
mininet/util/install.sh -n

```

*To verify :*

```
sudo mn --version

```


Quick Verify:
=============

Open 4 Terminals:


1. In Terminal1,

```
sudo wireshark &
```
And start the capture for any interface.


2. In Terminal2, 

```
ryu-manager ryu.app.simple_switch_13

```

3. In Terminal3,


```
sudo mn --controller=remote,ip=127.0.0.1 --mac --switch=ovsk,protocols=OpenFlow13 --topo=single,4 
pingall

```

4. In Terminal 4,

```
sudo ovs-vsctl show

sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```

5. check the openflow messages in wireshark


References:
-------------
https://osrg.github.io/ryu/

http://ryu.readthedocs.io/en/latest/getting_started.html

http://mininet.org/

https://iperf.fr/

https://www.wireshark.org

https://www.openvswitch.org/
