from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('add-departamento/', views.NewDepartamentoView.as_view(), name='ingresar_departamento'),
    path('listar-departamentos/', views.DepartamentoListView.as_view(), name="departamento_all"),
]
