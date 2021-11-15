#./app/app.py
from flask import Flask,render_template,request,session,flash,url_for,redirect
from datetime import timedelta
from pickleshare import *
import re
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'clave-secreta'
db = PickleShareDB('miDB')

#-----------------------------------------------------------------------------------------------------
#                                   PRÁCTICA 4 
#-----------------------------------------------------------------------------------------------------

client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
dbm = client.SampleCollections        # Elegimos la base de datos de ejemplo




@app.route('/mongo',methods=['GET', 'POST'])
def mongo():
	# Encontramos los documentos de la coleccion "samples_friends"
    pokemons = dbm.samples_pokemon.find() # devuelve un cursor(*), no una lista ni un iterador
    
    #Declaramos variables que usaremos luego en el render_template
    error_p=None
    error_a =None
    error_d = None
    error_m = None
    msg = None
    msg_a = None
    msg_d = None
    msg_m = None
    addname = None
    delname = None
    modname = None

    # Sacamos los nombres de la base de datos para mostrarlos al principio
    lista_nombre_pokemons = []
    
    for poke in pokemons:
        app.logger.debug(poke) # salida consola
        lista_nombre_pokemons.append(poke["name"])
    

    # Obtenemos los datos de los formularios, como hay varios formularios usamos el metodo .get para que no nos
    # levante un error si no hay nada escrito en los campos
    if request.method == 'POST':
        pokename = request.form.get('name')
        addname = request.form.get('name_a')
        delname = request.form.get('name_d')
        modname = request.form.get('modname')
        height = request.form.get('height')
        weight = request.form.get('weight')

        # Metodo para buscar un pokemon si el nombre existe devuelve documento de ese pokemon
        if pokename != None:
            if pokename in lista_nombre_pokemons:
                msg = dbm.samples_pokemon.find({"name":pokename})
            elif pokename == '':
                error_p = 'Escriba algun nombre para buscar el Pokemon'
            else:
                error_p = ' El pokemon no existe o no esta registrado en la base de datos'
        
        # Metodo para añadir un pokemon, lo añade en la base de datos unicamente con el atributo nombre
        if addname != None:
            if addname != '':
                dbm.samples_pokemon.insert_one({"name" : addname})
                msg_a = "Pokemon \'{}\' añadido con éxito.".format(addname)
                lista_nombre_pokemons.append(addname) 
            else:
                error_a = ' El campo no puede estar vacío'
        
        # Metodo para eliminar un pokemon si el nombre existe elimina el documento de ese pokemon de la base de datos
        if delname != None:
            if delname != '':
                if delname in lista_nombre_pokemons:
                    dbm.samples_pokemon.delete_one({"name" : delname})
                    msg_d = "Pokemon \'{}\' borrado con éxito.".format(delname)
                    lista_nombre_pokemons.remove(delname) 
                else: 
                    error_d = ' El pokemon \'{}\'  no existe y no puede ser borrado'.format(delname)
            else:
                error_d = ' El campo no puede estar vacío'
        
        # Metodo para modificar un pokemon, si el nombre existe modifica el o los campos que se hayan escrito en del documento de ese pokemon
        if modname != None:
            if modname != '':
                if modname in lista_nombre_pokemons:
                    if height != '' or weight != '':
                        if height == '':
                            dbm.samples_pokemon.update_one({"name" : modname},{"$set":{"weight":weight}})

                        elif weight == '':
                            dbm.samples_pokemon.update_one({"name" : modname},{"$set":{"height":height}})
                           
                        else:
                            dbm.samples_pokemon.update_one({"name" : modname},{"$set":{"height":height,"weight":weight}})
                        
                        msg_m = "Pokemon \'{}\' actualizado con éxito.".format(modname)

                    else:
                         error_m = ' Alguno de los campos a modificar debe estar rellenado'

                else:
                    error_m = ' El pokemon \'{}\' no existe por lo que no se puede modificar'.format(modname)
            else:
                error_m = ' El campo nombre no puede estar vacío'
            

    return render_template('base.html',
                            pokemons=lista_nombre_pokemons,
                            msg=msg,msg_a=msg_a,msg_d=msg_d,msg_m=msg_m,
                            error_p=error_p,error_a=error_a,error_d=error_d,error_m=error_m
                        )

#-----------------------------------------------------------------------------------------------------
#                                   FIN DE PRÁCTICA 4 
#-----------------------------------------------------------------------------------------------------



@app.route('/')
    

@app.route('/index')
def index():
    if 'link_1' not in session:
        init_link()
    links('index','Indice')
    return render_template('base.html', title='Welcome')


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    error = None
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        if username in db.keys() and db[username] == pwd :
            session['username'] = username
            session['password'] = pwd
            return redirect(url_for('index'))
        else:
            error = 'Usuario o contraseña incorrectos'
            
    return render_template('login.html', error=error)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    
    error = None
    username = None

    if request.method == 'POST':
        if request.form['username'] == '' or \
                request.form['password'] == '':
            error = 'Ningun campo puede esta vacío'
            return render_template('signin.html', error=error)
        else:
            username = request.form['username']
            pwd= request.form['password']
            db[username] = pwd
            session['username'] = username
            session['password'] = pwd
            return render_template('base.html')
    return render_template('signin.html', error=error)

@app.route('/logout')
def logout():
    
    session.pop('username',None)
    session.pop('password',None)
    session
    return render_template('base.html')

@app.route('/perfil')
def perfil():
    links('perfil','Perfil')
    return render_template('perfil.html')

@app.route('/ajustes', methods=['GET', 'POST'])
def ajustes():
    links('ajustes','Ajustes')

    error = None
    username = None

    if request.method == 'POST':
        if request.form['username'] == '' or \
                request.form['password'] == '':
            error = 'Ningun campo puede esta vacío'
            return render_template('ajustes.html', error=error)
        else:
            username = request.form['username']
            pwd= request.form['password']
            db.pop(session['username'])
            db[username] = pwd
            session['username'] = username
            session['password'] = pwd
            return render_template('base.html')
    return render_template('ajustes.html', error=error)

@app.route('/ejercicios')
def start():
    links('ejercicios','Ejercicios')
    return render_template('ejercicios.html', title='Welcome')




def links(link,name):
    """
    session['link_2']=session['link_1']
    session['n_2']=session['n_1']
    session['link_3']=session['link_2']
    session['n_3']=session['n_2']
    session['link_1']=url_for(link)
    session['n_1']=name

    return render_template('ejercicios.html', title='Welcome')
"""



def init_link():
    session['link_1']=0
    session['n_1']=''
    session['link_2']=0
    session['n_2']=''
    session['link_3']=0
    session['n_3']=''














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
    return render_template('error.html', title='ERROR')
	
