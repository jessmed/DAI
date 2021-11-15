# mi_aplicacion/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Libro(models.Model):
  titulo = models.CharField(max_length=200)
  autor  = models.CharField(max_length=100)

  def __str__(self):
    return self.titulo
  class Meta:
    permissions = (("can_mark_returned", "Set book as returned"),)

class Prestamo(models.Model):
  libro   = models.ForeignKey(Libro, on_delete=models.CASCADE, default="")
  fecha   = models.DateField(default=timezone.now)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    fech = self.fecha.strftime("%d/%m/%Y")
    id = self.libro.titulo+' - '+ fech
    return id
  
