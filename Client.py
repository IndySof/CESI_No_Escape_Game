#!/usr/bin/env python
import socket
def client_program():

    host = "82.165.48.44"
    port = 3232 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print(f"Connecting to {host}:{port}")
    sock.connect(server_address)
    while True:
        message = input('Saisir Message ("quit" = stop le programme) : ')
        if message == "quit" :
            sock.close()
            break
        sock.sendall(message.encode())

if __name__ == '__main__':
    client_program()