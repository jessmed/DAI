from django import forms
from django.utils import timezone
from django.db import models
from .models import Libro,Prestamo

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields =('titulo','autor')

class PrestamoForm_add(forms.ModelForm):
    class Meta:
        model = Prestamo
        exclude = ['fecha']

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        exclude = '__all__'




    