import random
import numpy as np
from time import time

#---------------Ejercicio 2-----------------------
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

#---------------Ejercicio 3-----------------------
def cribaEratostenes(n):
	primos = []
	isPrime = [1 for i in range(n)]
	isPrime[0] = isPrime[1] = 0

	for i in range(n):
		if isPrime[i]:
			primos.append(i)
			h = 2
			while i*h < n:
				isPrime[i*h] = 0
				h += 1

	return(primos)

#---------------Ejercicio 4-----------------------
def Fibonacci(n):
    if n < 2:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

#---------------Ejercicio 5-----------------------
def check(s):
   if len(s) % 2 != 0 or len(s)==0:
       return(False)
   else:
        i = 0
        r=0
        
        while r < len(s):
            if s[r] == "[":
                i += 1
            else:
                i -= 1
            r+=1
            if i < 0:
                return False
                
        if i != 0:
            return(False)
        else:
            return(True)

#---------------Ejercicio 6-----------------------
