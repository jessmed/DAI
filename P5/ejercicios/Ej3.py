# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:00:29 2020

@author: medye
"""
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
        
def main():
    print("Inserte un numero")
    n=int(input())
    primos = cribaEratostenes(n)
    print(primos)
    

if __name__ == "__main__":
    main()