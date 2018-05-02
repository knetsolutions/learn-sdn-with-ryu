#!/usr/bin/python


"""Custom topology example

Two directly connected switches plus a host for each switch:

   host1 --- switch1 --- switch2 --- host2

1. do pingall
2. Add a host3, switch3
3. Add a Link host3 to switch3
4. Add a Link swith2 to switch3
5. do pingall
6. cli
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from time import sleep


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        h1 = self.addHost('h1', mac="00:00:00:00:11:11", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:11:12", ip="192.168.1.2/24")

        self.addLink(h1, s1)
        self.addLink(h2, s2)

        self.addLink(s1, s2)


# This program is Not working - To be looked

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    sleep(5)
    net.pingAll()

    # add host
    net.addHost('h3')
    h3 = net.get('h3')
    h3.setIP('192.168.1.3/24')

    net.addSwitch('s3')
    s3 = net.get('s3')

    net.addLink(s3, h3)

    s2 = net.get('s2')
    net.addLink(s2, s3)
    net.build()
    net.pingAll()

    CLI(net)
    net.stop()
