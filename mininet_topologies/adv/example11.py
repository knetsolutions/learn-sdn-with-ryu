#!/usr/bin/python


"""Custom topology example

Two directly connected switches plus a host for each switch:

   host1 --- switch1 --- switch2 --- host2

1. do pingall
2. bring down the link (switch1 to switch2)
3. do pingall
4. bring up the link (switch1 to switch2)
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


if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    sleep(5)
    net.pingAll()

    # link down s1 to s2
    net.configLinkStatus('s1', 's2', 'down')
    net.pingAll()

    # link up s1 to s2
    net.configLinkStatus('s1', 's2', 'up')
    net.pingAll()

    CLI(net)
    net.stop()
