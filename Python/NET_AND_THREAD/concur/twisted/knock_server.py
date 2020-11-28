

from twisted.internet import protocol, reactor
class Knock(protocol, Protocol):
		def dataReceived(self, data):
				print 'Client:', data
				if data.startswith('Knock knock'):
						response = 'Whos there?'
				else:
						response = data + " who?"
				print 'Server':,response
				self.transport.write(response)

class KnockFactory(protocol, Factory):
		def buildProtocol(self, addr):
				return Knock()

reacrot.listenTCP(8000, KnockFactory())
reacrot.run()