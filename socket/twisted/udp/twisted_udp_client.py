from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

from socket import SOL_SOCKET, SO_BROADCAST


class EchoClientDatagramProtocol(DatagramProtocol):
    strings = [
        "Hello, world!",
        "What a fine day it is.",
        "Bye-bye!"
    ]

    def startProtocol(self):
        self.transport.socket.setsockopt(SOL_SOCKET, SO_BROADCAST, True)
        self.sendDatagram()

    def sendDatagram(self):
        if len(self.strings):
            datagram = self.strings.pop(0)
            self.transport.write(datagram.encode("utf-8"), ('127.0.0.1', 8888))
        else:
            reactor.stop()

    def datagramReceived(self, datagram: bytes, host):
        print('Datagram received: ', repr(datagram.decode("utf-8")))
        self.sendDatagram()


def main():
    protocol = EchoClientDatagramProtocol()
    # 0 means any port
    t = reactor.listenUDP(0, protocol)
    reactor.run()


if __name__ == '__main__':
    main()
