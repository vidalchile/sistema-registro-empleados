from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar-empleados/', views.ListAllEmpleados.as_view(), name="empleados_all"),
    path('lista-empleados-admin/', views.ListEmpleadosAdmin.as_view(), name="empleados_admin"),
    path('lista-by-area/<shortname>', views.ListByAreaEmpleados.as_view(), name="empleados_por_departamento"),
    path('lista-by-trabajo/<job>', views.ListByJobEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadoByKword.as_view()),
    path('habilidades/<id>', views.ListHabilidadesEmpleado.as_view()),
    path('ver-detalle-empleado/<pk>', views.EmpleadoDetailView.as_view(), name="ver_empleado"),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name="add_empleado"),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]