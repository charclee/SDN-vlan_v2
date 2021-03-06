from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm

if '__main__' == __name__:

	net=Mininet(controller=RemoteController)
	c0 = net.addController('c0',ip='192.168.99.101',port=6633)
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')
	s4 = net.addSwitch('s4')

	h1 = net.addHost('h1',mac='00:00:00:00:00:01')
	h2 = net.addHost('h2',mac='00:00:00:00:00:02')
	h3 = net.addHost('h3',mac='00:00:00:00:00:03')
	h4 = net.addHost('h4',mac='00:00:00:00:00:04')
	h5 = net.addHost('h5',mac='00:00:00:00:00:05')

	net.addLink(s1, h1)
	net.addLink(s2, h2)
	net.addLink(s3, h3)
	net.addLink(s3, h4)
	net.addLink(s1, s2,port1=30,port2=30)
	net.addLink(s1, s3,port1=40,port2=30)
	net.addLink(s2, s3,port1=40,port2=40)

	net.addLink(s4, h5)
	net.addLink(s1, s4,port1=50,port2=30)
	

	net.build()
	c0.start()
	s1.start([c0])
	s2.start([c0])
	s3.start([c0])
	s4.start([c0])

	net.terms.append(makeTerm(s1))
	net.terms.append(makeTerm(s2))

	CLI(net)
	net.stop()
