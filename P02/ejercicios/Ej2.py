# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:28:47 2020

@author: medye
"""
import random
import numpy as np
from time import time

def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def insertionSort(arr): 
    for i in range(1, len(arr)): 
  
        key = arr[i] 

        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
        
def main():
    m = np.random.randint(100,size=2000)
    n = m.copy()
    
    #Primer algoritmo ordenación
    t1_s = time()
    bubbleSort(m)
    t1 = time() - t1_s
    
    #Segundo algoritmo ordenación
    t2_s = time()
    insertionSort(n)
    t2 = time() - t2_s
    
    print("Bubble sort: ",t1,"s.")
    print("Insertion sort: ",t2,"s")
    

if __name__ == "__main__":
    main()