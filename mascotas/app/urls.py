from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_mascotas, name='listar_mascotas'),
    path('buscar/', views.buscar_mascotas, name='buscar_mascotas'),
    path('agregar/', views.agregar_mascota, name='agregar_mascota'),
]
