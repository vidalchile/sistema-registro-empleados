from django.contrib import admin
from django.urls import path

# . significa que voy a importar un archivo que esta en la misma carpeta, está en la misma altura
from . import views

urlpatterns = [
    path('prueba-home', views.PruebaView.as_view()),
    path('prueba-list-view', views.PruebaListView.as_view()),
    path('prueba-lista', views.ListarPrueba.as_view()),
    path('prueba-add', views.PruebaCreateView.as_view(), name='prueba_add'),
]
