import socket
import sys

from recorder import Recorder
from configparser import ConfigParser
print ("\n")
print (" /$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$        /$$$$$$  /$$       /$$$$$$ /$$$$$$$$ /$$   /$$ /$$$$$$$$" )
print(" /$$__  $$| $$_____/ /$$__  $$|_  $$_/       /$$__  $$| $$      |_  $$_/| $$_____/| $$$ | $$|__  $$__/")
print("| $$  \__/| $$      | $$  \__/  | $$        | $$  \__/| $$        | $$  | $$      | $$$$| $$   | $$   ")
print("| $$      | $$$$$   |  $$$$$$   | $$        | $$      | $$        | $$  | $$$$$   | $$ $$ $$   | $$   ")
print("| $$      | $$__/    \____  $$  | $$        | $$      | $$        | $$  | $$__/   | $$  $$$$   | $$   ")
print("| $$    $$| $$       /$$  \ $$  | $$        | $$    $$| $$        | $$  | $$      | $$\  $$$   | $$   ")
print("|  $$$$$$/| $$$$$$$$|  $$$$$$/ /$$$$$$      |  $$$$$$/| $$$$$$$$ /$$$$$$| $$$$$$$$| $$ \  $$   | $$   ")
print("\______/ |________/ \______/ |______/       \______/ |________/|______/|________/|__/  \__/   |__/    ")
print ("\n")

config = ConfigParser() 
config.read('config.ini')


def selecteur():
    print("=============================================")
    print(" Si vous voulez envoyer un message vocal -> 1")
    print(" Si vous voulez envoyer un message écrit -> 2")
    print("=============================================")

    rep = int(input())

    if rep == 1 : 
        voix()
    elif rep == 2 :
        message()
    else: 
        print("Nombre invalide")
        
host = config.get('settings', 'host')
port = int(config.get('settings', 'port'))
print(f"Connexion à {host}:{port}")


def voix():
    r = Recorder()
    print("Enregistrement ...")
    r.record(5, output='out1.wav')  
    print("Enregistrement terminé")


    s = socket.socket()
    s.connect((host,port))
    f = open ("out1.wav", "rb")
    l = f.read(1024)
    s.sendall("voc".encode())

    while (l):
        s.send(l)
        l = f.read(1024)
    s.close()

def message(): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    sock.connect(server_address)
    sock.sendall("txt".encode())
    while True:
        message = input('Saisir Message ("quit" = stop le programme) : ')
        if message == "quit" :
            sock.close()
            break
        sock.sendall(message.encode())


if __name__ == '__main__':
    selecteur()