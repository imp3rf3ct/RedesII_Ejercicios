#!/usr/bin/env python
import struct

def openfile():
    return open('ListinEmpaquetado.out','w')

def main():
    arch = openfile()
    listado = [22,55,696587878,678454784,256]

    paquete = struct.pack('!BBIIH',listado[0],listado[1],listado[2],listado[3],listado[4])

    arch.write(paquete+"\n")

main()
