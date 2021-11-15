# mi_aplicacion/views.py

from django.shortcuts import render, HttpResponse,redirect
from .forms import LibroForm, PrestamoForm,PrestamoForm_add
from django.views import generic
from .models import Libro,Prestamo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.decorators import permission_required

# Create your views here.
@login_required
def libro(request):
    libros = Libro.objects.all()
    return render(request,'libro.html',{'libros':libros})

@login_required
def prestamo(request):
    prestamos = Prestamo.objects.all()
    return render(request,'prestamo.html',{'prestamos':prestamos})

def index(request):
    return render(request,'index.html')

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def libro_nuevo(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
            return redirect('/libro')
    else:
        form = LibroForm()
    return render(request, 'libro_nuevo.html', {'form': form})

@permission_required('catalog.can_mark_returned')
@login_required
def libro_edit(request,libro_id):
    instancia = Libro.objects.get(id=libro_id)
    form = LibroForm(instance=instancia)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=instancia)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
            return redirect('/libro')
    else:
        form = LibroForm(instance=instancia)
    return render(request, 'libro_edit.html', {'form': form})

@permission_required('catalog.can_mark_returned')
@login_required
def libro_borrar(request,libro_id):
    instancia = Libro.objects.get(id=libro_id)
    instancia.delete()
    
    return redirect('/libro')





@login_required
def prestamo_nuevo(request):
    if request.method == "POST":
        form = PrestamoForm_add(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.usuario = request.user
            prestamo.fecha = timezone.now()
            prestamo.save()
            return redirect('/prestamo')
    else:
        form = PrestamoForm_add()
    return render(request, 'prestamo_nuevo.html', {'form': form})

@permission_required('catalog.can_mark_returned')
@login_required
def prestamo_edit(request,prestamo_id):
    instancia = Prestamo.objects.get(id=prestamo_id)
    form = PrestamoForm(instance=instancia)
    if request.method == "POST":
        form = PrestamoForm(request.POST, instance=instancia)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.save()
            return redirect('/prestamo')
    else:
        form = PrestamoForm(instance=instancia)
    return render(request, 'prestamo_edit.html', {'form': form})

@permission_required('catalog.can_mark_returned')
@login_required
def prestamo_borrar(request,prestamo_id):
    instancia = Prestamo.objects.get(id=prestamo_id)
    instancia.delete()
    
    return redirect('/prestamo')


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('home')
    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})