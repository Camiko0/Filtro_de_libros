# -*- coding: utf-8 -*-
from Pila import *
from Cola import *

class logica:
    
    """ INSTANCIAS Y VARIABLES"""
    def __init__(self):
        #Instancia a la clase Cola y creación de la cola
        cola = Cola()
        pila = Pila()
        # Variables
        contador = 1
        #Join para reemplazar ', 'y strip para eliminar '[]'
        impresion = "Titulo, Autor, Tematica , Paginas , Editorial" + '\n' + '\n'
        #Ordenar por paginas
        impresion += self.ordenar_paginas(self.agregar_cola(cola),pila,contador)
        #Ordenar por titulo
        impresion += self.ordenar_otros(self.agregar_cola(cola),pila,contador, 0)
        #Ordenar por Autor
        impresion += self.ordenar_otros(self.agregar_cola(cola),pila,contador, 1)
        #Ordenar por Tematica
        impresion += self.ordenar_otros(self.agregar_cola(cola),pila,contador, 2)
        #Ordenar por Editorial
        impresion += self.ordenar_otros(self.agregar_cola(cola),pila,contador, 4)
        #Poner el resultado en el archivo busquedas.txt
        self.escribir_archivo(impresion)

    """ AGREGAR ELEMENTOS A LA COLA """
    def agregar_cola(self,cola):
        libros = open("libros.txt")
        linea = libros.readline()
        while linea != '':
            linea = libros.readline()
            if (linea == ''):
                libros.close()
                break
            cola.encolar(linea.split(','))
        return cola

    """ AGREGAR EL RESULTADO AL ARCHIVO """
    def escribir_archivo(self,resultado):
        busquedas = open("busquedas.txt", "w")
        busquedas.write(resultado)
        busquedas.close()
        
    """ ORDENAR POR NUMERO DE PAGINAS (MENOR A MAYOR)"""
    def ordenar_paginas(self,cola,pila,contador):
        impresion = '\n ORDENAR POR PAGINAS (MENOR A MAYOR): \n'
        #Mientras hallan elementos en la cola o pila
        while cola.es_vacia() == False or pila.es_vacia() == False:
            lista = cola.desencolar()
            #Mientras hallan elementos en la cola
            while cola.es_vacia() == False:
                lista2 = cola.desencolar()
                #Comparación entre dos elementos de la cola / El menor se queda y el mayor se agrega a la pila
                if int(lista[3]) < int(lista2[3]):
                    pila.apilar(lista2)
                else:
                    pila.apilar(lista)
                    lista = lista2
            #Agregar el menor elemento a la impresión
            impresion += str(contador) +') '+', '.join(map(str, lista)).strip('[]')
            contador += 1
            #Se mueven todos los elementos de la pila a la cola
            while pila.es_vacia() == False:
                cola.encolar(pila.desapilar())
        return impresion

    """ ORDENAR POR TITULO (A-Z)"""
    def ordenar_otros(self,cola,pila,contador, opcion):
        if opcion ==0:
            impresion = '\n ORDENAR POR TITULO (A-Z): \n'
        elif opcion ==1:
            impresion = '\n ORDENAR POR AUTOR (A-Z): \n'
        elif opcion==2:
            impresion = '\n ORDENAR POR TEMATICA (A-Z): \n'
        else:
            impresion = '\n ORDENAR POR EDITORIAL (A-Z): \n'
        #Mientras hallan elementos en la cola o pila
        while cola.es_vacia() == False or pila.es_vacia() == False:
            lista = cola.desencolar()
            #Mientras hallan elementos en la cola
            while cola.es_vacia() == False:
                lista2 = cola.desencolar()
                #Comparación entre dos elementos de la cola / El menor se queda y el mayor se agrega a la pila
                #ord para convertir a condigo ascii               
                if int(ord(lista[opcion][0])) == int(ord(lista2[opcion][0])):
                    x = 1
                    while int(ord(lista[opcion][x])) == int(ord(lista2[opcion][x])) and x < len(lista[opcion])-1:
                        x += 1
                    if int(ord(lista[opcion][x])) < int(ord(lista2[opcion][x])):
                        pila.apilar(lista2)
                    else:
                        pila.apilar(lista)
                        lista = lista2  
                else:
                    if int(ord(lista[opcion][0])) < int(ord(lista2[opcion][0])):
                        pila.apilar(lista2)
                    else:
                        pila.apilar(lista)
                        lista = lista2
            #Agregar el menor elemento a la impresión
            impresion += str(contador) +') '+', '.join(map(str, lista)).strip('[]')
            contador += 1
            #Se mueven todos los elementos de la pila a la cola
            while pila.es_vacia() == False:
                cola.encolar(pila.desapilar())
        return impresion

log = logica()
