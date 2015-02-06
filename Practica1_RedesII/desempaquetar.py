#!/usr/bin/env python
import struct

def openfiler():
    return open('./ListinLlamadas','r')

def openfilew():
    return open('./ListinLlamadas2','w')

def imprimirlistado(listin_llamada):
    for el in listin_llamada:
        print el

def desempaquetado():
    cont = 0
    listado = []
    cad = ""
    
    arch = openfiler()

    for el in arch:
        cont = cont + len(el)
        cad = cad + el
        
        if cont == 12:
            listado.append(struct.unpack('!BBIIH',cad))
            cont = 0
            cad = ""
    
    arch.close()
    return listado
    
def empaquetado(listin_llamada):
    cont = 0
    arch = openfilew()

    for el in listin_llamada:
        arch.write(struct.pack('!B',el[0]))
        arch.write(struct.pack('!BIIH',el[1],el[2],el[3],el[4]))

    arch.close()

def main():
    listin_llamada = desempaquetado()
    
    imprimirlistado(listin_llamada)
    
    empaquetado(listin_llamada)
        
    #Fin del programa

main()
