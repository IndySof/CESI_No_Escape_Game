import socket
import sys

from configparser import ConfigParser

print("\n")
print('  /$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$        /$$$$$$  /$$$$$$$$ /$$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$ ')
print(' /$$__  $$| $$_____/ /$$__  $$|_  $$_/       /$$__  $$| $$_____/| $$__  $$| $$   | $$| $$_____/| $$__  $$')
print('| $$  \__/| $$      | $$  \__/  | $$        | $$  \__/| $$      | $$  \ $$| $$   | $$| $$      | $$  \ $$')
print('| $$      | $$$$$   |  $$$$$$   | $$        |  $$$$$$ | $$$$$   | $$$$$$$/|  $$ / $$/| $$$$$   | $$$$$$$/')
print('| $$      | $$__/    \____  $$  | $$         \____  $$| $$__/   | $$__  $$ \  $$ $$/ | $$__/   | $$__  $$')
print('| $$    $$| $$       /$$  \ $$  | $$         /$$  \ $$| $$      | $$  \ $$  \  $$$/  | $$      | $$  \ $$')
print('|  $$$$$$/| $$$$$$$$|  $$$$$$/ /$$$$$$      |  $$$$$$/| $$$$$$$$| $$  | $$   \  $/   | $$$$$$$$| $$  | $$')
print(' \______/ |________/ \______/ |______/       \______/ |________/|__/  |__/    \_/    |________/|__/  |__/')
print("\n")                                                                                                     
                                                                                                         
                                                                                                         
                                                                                                                                                                                                       

config = ConfigParser() 
config.read('config.ini')



s = socket.socket()
host = config.get('settings', 'host')
port = int(config.get('settings', 'port'))

s.bind((host,port))
s.listen(10) 
print(f"Le serveur démarre sur {host}:{port}")
while True:
    sc, address = s.accept()

    print (address)
    i=1
    f = open("out1.wav",'wb') 
    i=i+1

    l = sc.recv(3).decode()
    if l == "voc":
        while (True):       
            l = sc.recv(1024)
            while (l):
                f.write(l)
                l = sc.recv(1024)
        f.close()


    elif l == "txt":
        while True:
            l = sc.recv(1024).decode()
            print(l)
    else:
        print("Protocole Inconnu : ", l)
    sc.close()

s.close()