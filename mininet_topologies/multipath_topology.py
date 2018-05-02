#!/usr/bin/python


"""Multipath topo example

Ring Topology( Multipath),

Switch1-----Switch2------Switch3-----Switch4-----switch1

Switch1-----Host1
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
        s4 = self.addSwitch('s4')

        a1 = self.addHost('a1', mac="00:00:00:00:11:11", ip="192.168.1.1/24")
        b1 = self.addHost('b1', mac="00:00:00:00:11:12", ip="192.168.1.2/24")

        self.addLink(s1, a1, 1, 1)
        self.addLink(s4, b1, 1, 1)

        self.addLink(s1, s2, 2, 1)
        self.addLink(s2, s4, 2, 2)
        self.addLink(s1, s3, 3, 1)
        self.addLink(s3, s4, 2, 3)


if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    sleep(5)
    print("Topology is up, lets ping")
    net.pingAll()
    CLI(net)
    net.stop()
