#!/usr/bin/env python
import struct

def openfile():
    return open('ListinEmpaquetado.out','w')

def main():
    arch = openfile()
    listado = [[22,55,696587878,678454784,256],[19,20,694583478,677874584,60]]
    for el in listado:
        paquete = struct.pack('!BBIIH',el[0],el[1],el[2],el[3],el[4])
        arch.write(paquete+"\n")

main()
