#./app/app.py
from flask import Flask, send_from_directory
import re


app = Flask(__name__)
          
@app.route('/')
def start():
    return send_from_directory(filename="index.html",directory="static")

#Ejercicio 2
@app.route('/ordena/<arr>')
def insertionSort(arr): 
    arr = arr.split(',')
    #Importante hacer esta conversion a int porque si no el algoritmo no funciona bien
    #y hace la comparaciones con strings y siempre prioriza el primer dígito
    arr = list(map(int, arr))

    for i in range(1, len(arr)): 
  
        key = arr[i] 

        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    arr = list(map(str, arr))
    arr = ",".join(arr)

    return("{}".format(arr))
 





#Ejercicio 3	
@app.route('/cribaEratostenes/<int:n>')
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

	return("{}".format(primos))

#Ejercicio 4
@app.route('/fibonacci/<int:n>')
def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
    return("El número {} de la sucesión de Fibonacci es {}".format(n,  b))

#Ejercicio 5
@app.route('/checkParentesis/<s>')
def check(s):
   if len(s) % 2 != 0 or len(s)==0:
       return("False")
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
                return("Parentesis string is False")
                
        if i != 0:
            return("Parentesis string is False")
        else:
            return("Parentesis string is True")

#Ejercicio 6
@app.route('/regex/<s>')
def reg(s):
    a = re.search("([\w]+) ([\w]{1})$",s)        
    t = re.search("[\d]{4}( |-)[\d]{4}( |-)[\d]{4}( |-)[\d]{4}$",s)
    c = re.search("([\w.-]+)@([\w.-]+)", s)
    if a:
        return("Inicial apellido: {}".format(a.group(0)))
    if t:
        return("Tarjeta: {}".format(t.group(0)))
    if c:
        return("Email: {}".format(c.group(0)))

@app.errorhandler(404)
def not_found(error):
    return send_from_directory(filename="error.html",directory="static")

    
	
