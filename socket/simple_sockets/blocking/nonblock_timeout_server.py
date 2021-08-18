import socket
from os import system

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))

sock.listen(5)
sock.settimeout(5)

any_connection = True
while True:
    try:
        client, addr = sock.accept()

    except socket.error:
        if any_connection is True:
            print("No connections!")
            any_connection = False

    except KeyboardInterrupt:
        break

    else:
        any_connection = True

        print("\nConnected!")

        result = client.recv(1024).decode("utf-8")
        client.close()

        print("Message:\n"
              f"{result}\n")
