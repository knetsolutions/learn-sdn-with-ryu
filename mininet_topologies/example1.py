#!/usr/bin/python

"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from time import sleep



class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(s1, s2)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    net = Mininet(topo)
    net.start()
    sleep(5)
    net.pingAll()
    #CLI(net)
    net.stop()
