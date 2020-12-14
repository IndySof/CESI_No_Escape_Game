#!/usr/bin/env python

import socket


def server_program():
    host = "82.165.48.44"
    port = 3232

    server_socket = socket.socket()  
 
    server_socket.bind((host, port))  

    print(f"Starting Server on {host}:{port}")
    server_socket.listen(2)
    while True:
        conn, address = server_socket.accept() 
        try: 
         while True:
            data = conn.recv(32)
            if data:
                print (f"message : {data}")

            
        finally:
         # Clean up the connection
         connection.close()


if __name__ == '__main__':
    server_program()