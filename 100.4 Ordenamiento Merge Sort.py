# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:17:19 2023

@author: 52331
"""

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
    
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
    
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
            
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        
    
    return sorted_list

def mergeSort (nums):

    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2

    left_list = mergeSort(nums[:mid])
    right_list = mergeSort(nums[mid:])

    return merge(left_list, right_list)

listaNumerosAleatorios = [5, 2, 1, 8, 4]
print("Lista sin ordenar: " + str(listaNumerosAleatorios))
listaNumerosAleatorios = mergeSort(listaNumerosAleatorios)
print("Lista ordenada: " + str(listaNumerosAleatorios))

