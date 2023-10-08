# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:22:02 2023

@author: 52331
"""

def bubbleSort (nums) :
    #Establecemos la variable intercambio en True para entrar en el bucle al menos una vez
    intercambio = True
    while intercambio:
            intercambio = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i +1]:
                    #Intercambiamos los datos
                    nums[i], nums[i +1] = nums[i + 1], nums[i]
                    intercambio = True
                    #Cambiamos a True la variable ya que ha habido un intercambio
            

#Comprobamos el funcionamiento
listaNumerosAleatorios = [5, 2, 1, 8, 4]
bubbleSort (listaNumerosAleatorios)
print(listaNumerosAleatorios)
