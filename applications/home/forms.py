from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        #fields = ('__all__')
        fields = ('titulo', 'subtitulo', 'cantidad')
        widgets = {
            'cantidad': forms.TextInput(
                attrs = {
                    'placeholder':'ingresar cantidad'
                }
            ),
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder':'ingresar titulo'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs = {
                    'placeholder':'ingresar subtitulo'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('El campo cantidad debe ser mayor a 10')
        return cantidad
