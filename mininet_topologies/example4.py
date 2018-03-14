#!/usr/bin/python


"""Custom topology example

Two directly connected switches plus a host for each switch:

   host1 --- switch --- switch --- host2

Triggers the IPERF Traffic from host1 to host2

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


if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    sleep(5)
    net.pingAll()

    # get the host objects
    h1 = net.get('h1')
    h2 = net.get('h2')
    h1.cmd('iperf -s &')
    result = h2.cmd('iperf -c 192.168.1.1')
    print result
    CLI(net)
    net.stop()
