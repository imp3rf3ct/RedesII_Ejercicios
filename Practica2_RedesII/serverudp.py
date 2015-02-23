#!/usr/bin/env python3

from socket import *
import _thread
import sys
def enviardatos(sock,client):
    while 1:
        data = input()
        enviar = data.encode()
        sock.sendto(enviar,client)
        if data == "bye":
            print("Closing Server\n")
            sock.close()
            sys.exit(0)
            break

def recibirdatos(sock):
    msg,client = sock.recvfrom(1024)
    msg = msg.decode()
    print(msg)
    if msg == "bye":
            print("Closing server\n")
            sock.close()
            return 0
    _thread.start_new_thread(enviardatos,(sock,client))
    while 1:
        try:
            msg,client = sock.recvfrom(1024)
        except OSError:
            sys.exit(0)

        msg = msg.decode()
        print(msg)
        if msg == "bye":
            print("Closing server\n")
            sock.close()
            sys.exit(0)
        
def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind(('',23456))
    recibirdatos(sock)

main()
