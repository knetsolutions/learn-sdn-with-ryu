#!/usr/bin/python


"""Grouptable example

Ring Topology(Tree),

Switch1-----Switch2
Switch1------Switch3-

Switch1-----
Switch4-----Host4


ryu stuff:

ryu-manager ryu.app.simple_switch_13

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController
from time import sleep


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        a1 = self.addHost('a1', mac="00:00:00:00:11:11", ip="192.168.1.1/24")
        b1 = self.addHost('b1', mac="00:00:00:00:11:12", ip="192.168.1.2/24")
        sniffer = self.addHost('sniffer', mac="00:00:00:00:11:13", ip="192.168.1.3/24")

        self.addLink(s2, a1, 1, 1)
        self.addLink(s3, b1, 1, 1)
        self.addLink(s1, sniffer, 1, 1)

        self.addLink(s2, s1, 2, 2)
        self.addLink(s3, s1, 2, 3)



if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    #sleep(5)
    #print("Topology is up, lets ping")
    #net.pingAll()
    CLI(net)
    net.stop()
