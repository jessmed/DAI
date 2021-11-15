from django import forms
from django.utils import timezone
from django.db import models
from .models import Libro,Prestamo
from django.contrib.auth.models import User

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields =('titulo','autor')

class PrestamoForm_add(forms.ModelForm):
    class Meta:
        model = Prestamo
        exclude = ['usuario','fecha']

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        exclude = '__all__'




    