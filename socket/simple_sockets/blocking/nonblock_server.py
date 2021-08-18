import socket
from os import system

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))

sock.listen(5)
sock.setblocking(False)

any_client = True
while True:
    try:
        client, addr = sock.accept()

    except socket.error:
        if any_client is True:
            print("No clients!")
            any_client = False

    except KeyboardInterrupt:
        break

    else:
        print("\nConnected!")

        client.setblocking(True)
        result = client.recv(1024).decode("utf-8")
        client.close()

        any_client = True
        print("Message:\n"
              f"{result}\n")
