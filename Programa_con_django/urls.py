from django.contrib import admin
from django.urls import path
from Programa_con_django import views
urlpatterns=[

    path('agregar_nombre/',views.nombre),
    path('buscar/',views.bienbenida),
]