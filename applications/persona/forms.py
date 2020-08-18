from django import forms
from .models import Empleado

class CrearEmpleadoForm(forms.ModelForm):
    """Formulario para crear un empleado."""

    class Meta:
        model = Empleado
        fields = (
            'firt_name', 
            'last_name',
            'full_name',
            'job',
            'departamento',
            'habilidades',
            'avatar'
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }