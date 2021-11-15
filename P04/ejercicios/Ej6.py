# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:47:16 2020

@author: medye
"""
import re
     
def main():
    txt = "Apellido N"
      
    apellido = re.search("([\w]+) ([\w]{1})$",txt)        
    tarjeta = re.search("[\d]{4}( |-)[\d]{4}( |-)[\d]{4}( |-)[\d]{4}$",txt)
    correo = re.search('([\w.-]+)@([\w.-]+)', txt)
   
   
if __name__ == "__main__":
    main()