import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = f"Hello World!"
sock.sendto(bytes(msg, 'utf-8'), ("127.0.0.1", 8888))

sock.close()
