# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:08:45 2023

@author: 52331
"""

def insertionSort(nums):
    #Entendemos que el primer elemento sin ordenar es el más pequeño
    #así que comenzamos con el segundo
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        #Guardamos en j el índice del elemento anterior
        j=i-1
        #Movemos todos los elementos de la lista hacia delante si son
        #mayores que el elemento a insertar
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j-=1
        #Insertamos el elemento
        nums[j + 1] = item_to_insert

#Comprobamos el funcionamiento

listaNumerosAleatorios = [5, 2, 1, 8, 4]

print("Lista sin ordenar: " + str(listaNumerosAleatorios))
insertionSort (listaNumerosAleatorios)

print("Lista ordenada: " + str(listaNumerosAleatorios))

