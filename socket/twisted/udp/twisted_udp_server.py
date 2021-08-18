from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from datetime import datetime


class EchoUDP(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        print(f"Received from address: {str(address)} at {datetime.now()}")
        print(datagram.decode("utf-8"))
        self.transport.write(datagram, address)
        print("Finished sending reply.")


print("Starting server.")
reactor.listenUDP(8888, EchoUDP())
reactor.run()
