# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:33:36 2020

@author: medye
"""
import random

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
                    
            
   
        
def main():
    #Creamos cadena parentesis
    s = "[]"
    p = "".join(random.choices(s,k=6))
    print(p)
    #Comprobamos si es correcta
    if check(p):
        print("Cadena correcta")
    else:
        print("Cadena incorrecta")
   
   
if __name__ == "__main__":
    main()