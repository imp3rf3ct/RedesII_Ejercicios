#!/usr/bin/env python3

from socket import *
import _thread
import sys
def enviardatos(sock):
    data = input()
    enviar = data.encode()
    sock.sendto(enviar,('localhost',23456))
    if data == "bye":
        print("Closing Client\n")
        sock.close()
        return 0
    
    _thread.start_new_thread(recibirdatos,(('localhost',23456),sock))
    while 1:
        data = input()
        enviar = data.encode()
        sock.sendto(enviar,('localhost',23456))
        if data == "bye":
            print("Closing Client\n")
            sock.close()
            break
        else:
            if data == "bye":
                print("Closing client\n")
                sock.close()
                sys.exit(0)

def recibirdatos(tupla,sock):
    while 1:
        try:
            msg,server = sock.recvfrom(1024)
        except OSError:
            sys.exit(0)

        data = msg.decode()
        print(data)
        if data == "bye":
            print("Closing client\n")
            sock.close()
            
    
def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    enviardatos(sock)
            

main()
