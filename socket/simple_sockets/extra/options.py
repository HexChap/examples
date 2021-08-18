import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(("127.0.0.1", 8888))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("8888 is bind")

    while True:
        result = sock.recv(1024).decode("utf-8")
        print("\nMessage:\n"
              f"{result}")
