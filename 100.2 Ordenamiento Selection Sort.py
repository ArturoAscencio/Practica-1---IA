# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:43:35 2023

@author: 52331
"""

def selectionSort(nums):
    #El valor de i correspondo al numero de datos que se ordenaron
    for i in range(len(nums)):
        #Entendemos que el primer elemento sin ordenar es el más pequeño
        lowest_value_index = i
        #Este bucle trabaja sobre los elementos no calsificados
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
                #Intercambia el valor del elemnentos sin ordenar mas bajo
                #con el primero sin ordenar
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

#Comprobamos el funcionamiento
listaNumerosAleatorios = [5, 2, 1, 8, 4]
print("Lista sin ordenar: " + str(listaNumerosAleatorios))
selectionSort(listaNumerosAleatorios)
print("Lista ordenada: " + str(listaNumerosAleatorios))

