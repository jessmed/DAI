# mi_aplicacion/views.py

from django.shortcuts import render, HttpResponse,redirect
from .forms import LibroForm, PrestamoForm,PrestamoForm_add
from django.views import generic
from .models import Libro,Prestamo

# Create your views here.
def libro(request):
    libros = Libro.objects.all()
    return render(request,'libro.html',{'libros':libros})

def prestamo(request):
    prestamos = Prestamo.objects.all()
    return render(request,'prestamo.html',{'prestamos':prestamos})

def index(request):
    return render(request,'index.html')


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


def libro_borrar(request,libro_id):
    instancia = Libro.objects.get(id=libro_id)
    instancia.delete()
    
    return redirect('/libro')






def prestamo_nuevo(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.save()
            return redirect('/prestamo')
    else:
        form = PrestamoForm_add()
    return render(request, 'prestamo_nuevo.html', {'form': form})

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

def prestamo_borrar(request,prestamo_id):
    instancia = Prestamo.objects.get(id=prestamo_id)
    instancia.delete()
    
    return redirect('/prestamo')