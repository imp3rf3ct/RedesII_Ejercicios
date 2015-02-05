#!/usr/bin/env python
import struct

def openfile():
    return open('./ListinEmpaquetado.out','r')

def main():
    listado = []
    arch = openfile()

    for el in arch:
        el = el.split('\n')[0]
        listado.append(struct.unpack('!BBIIH',el))
    
    arch.close()

    for el in listado:
        print (el)
        
    #Fin del programa

main()
