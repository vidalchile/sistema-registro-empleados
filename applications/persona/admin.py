from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    # columnas que vemos en nuestra tabla de empleados
    list_display = (
        'id',
        'firt_name',
        'last_name',
        'full_name',
        'departamento',
        'job',
        'direccion',
    )

    # columna creada por nosotros no existe en nuestro modelo
    def direccion(self, obj):
        return 'dirección de prueba'

    search_fields = ('firt_name',) # buscar por por nombre
    list_filter = ('departamento', 'job', 'habilidades', ) # filtrar por ...
    filter_horizontal = ('habilidades',) # editar campo de nuestro formulario

admin.site.register(Empleado, EmpleadoAdmin)


admin.site.register(Habilidades)