from django.contrib import admin

# Register your models here.
from .models import Libro, Prestamo

admin.site.register(Libro)
admin.site.register(Prestamo)