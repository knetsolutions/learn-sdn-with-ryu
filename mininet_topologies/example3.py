#!/usr/bin/python


"""Custom topology example

RING Topology(Loop),

Switch1-----Switch2------Switch3-----Switch4-----Switch1


Switch1-----Host1
Switch2-----Host2
Switch3-----Host3
Switch4-----Host4

MAC,IP, Controller, CLI stuff configured

# run RYU SDN STP Application for this topology

ryu-manager ryu.app.simple_switch_stp

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        h1 = self.addHost('h1', mac="00:00:00:00:11:11", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:11:12", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:11:13", ip="192.168.1.3/24")
        h4 = self.addHost('h4', mac="00:00:00:00:11:14", ip="192.168.1.4/24")

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    #net.pingAll()
    CLI(net)
    net.stop()
