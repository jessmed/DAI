# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:17:48 2020

@author: medye
"""
def Fibonacci(n):
    if n < 2:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
        
def main():
   #Leer fichero
   f = open("Numero.txt")
   n = int(f.read())
   f.close()
   print(n)

   #Calcular numero  y escribir en fichero
   f=open("Fibonacci.txt","w")
   f.write(str(Fibonacci(n)))
   f.close()
   
if __name__ == "__main__":
    main()