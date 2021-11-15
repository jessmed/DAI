# mi_aplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('home/', views.home, name='home'),
  path('libro/', views.libro, name='libro'),
  path('register/', views.register,name='register'),
  path('libro/nuevo/', views.libro_nuevo, name='libro_nuevo'),
  path('libro/edit/<int:libro_id>', views.libro_edit, name='libro_edit'),
  path('libro/borrar/<int:libro_id>', views.libro_borrar, name='libro_borrar'),
  path('prestamo/', views.prestamo, name='prestamo'),
  path('prestamo/nuevo/', views.prestamo_nuevo, name='prestamo_nuevo'),
  path('prestamo/edit/<int:prestamo_id>', views.prestamo_edit, name='prestamo_edit'),
  path('prestamo/borrar/<int:prestamo_id>', views.prestamo_borrar, name='prestamo_borrar'),

]