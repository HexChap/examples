import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(100):
    msg = f"{i+1}.Hello World!"
    sock.sendto(bytes(msg, 'utf-8'), ("127.0.0.1", 8888))
