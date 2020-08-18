from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('****************** funcion form_valid *********************')
        
        # forma 1 de crear un objeto
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname']
        )
        depa.save()

        # forma 2 de crear un objeto, no necesita funcion save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        Empleado.objects.create(
            firt_name = nombre,
            last_name = apellido,
            job = 1,
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)
