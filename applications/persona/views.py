from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
# models
from .models import Empleado
# form
from .forms import CrearEmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    """ listar todos los empleados de la empresa """
    template_name = 'persona/list_all.html'
    paginate_by = 3
    ordering = 'firt_name'
    #model = Empleado
    context_object_name = 'empleados'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(full_name__icontains = palabra_clave)
        return lista


class ListEmpleadosAdmin(ListView):
    """ listar todos los empleados de la empresa """
    template_name = 'persona/list_empleados.html'
    paginate_by = 4
    ordering = 'firt_name'
    model = Empleado
    context_object_name = 'empleados'


class ListByAreaEmpleados(ListView):
    """ listar todos los empleados que pertenecen a un area de la empresa """
    template_name = 'persona/list_by_area.html'
    model = Empleado
    context_object_name = "empleados"
    def get_queryset(self):
        # obtener valor parametro url
        area = self.kwargs['shortname']
        lista =Empleado.objects.filter(departamento__short_name = area)
        return lista


class ListByJobEmpleado(ListView):
    """ listar empleados por trabajo """
    template_name = 'persona/list_by_trabajo.html'
    model = Empleado

    def get_queryset(self):
        trabajo = self.kwargs['job']
        lista = Empleado.objects.filter(job = trabajo)
        return lista


class ListEmpleadoByKword(ListView):
    """ lista los empleados por palabra clave (info viene desde un formulario) """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(firt_name = palabra_clave)
        return lista


class ListHabilidadesEmpleado(ListView):
    """ lista todas las habilidades de un empleado """
    template_name = 'persona/habilidades_empleado.html'
    model = Empleado
    context_object_name = 'habilidades'

    def get_queryset(self):
        id = self.kwargs['id']
        empleado = Empleado.objects.get(id = id)
        return empleado.habilidades.all()


# ver en detalle un registro
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    context_object_name = 'empleado'
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # generando algun logica proceso
        context['titulo'] = 'ejm. context'
        return context



class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = CrearEmpleadoForm
    template_name = "persona/add.html"
    """
    fields = [
        'firt_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar'
    ]
    """
    #fields = ('__all__')
    #success_url = '.' # la misma pagina, redireccionar cuando esta todo correcto
    #success_url = '/success/'
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        """ If the form is valid, save the associated model. """
        #logica del proceso
        #empleado = form.save()
        empleado = form.save(commit=False)
        empleado.full_name = empleado.firt_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    form_class = CrearEmpleadoForm
    """
    fields = [
        'firt_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar'
    ]
    """
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        """ Handle POST requests: instantiate a form instance with the passed
            POST variables and then check if it's valid. """
        self.object = self.get_object()
        print("************* METODO POST **************")
        print(request)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """ If the form is valid, save the associated model. """
        #logica del proceso
        #empleado = form.save()
        print('====================================================')
        print('#=========== MODIFICAR EMPLEADO ===================#')
        empleado = form.save(commit=False)
        empleado.full_name = empleado.firt_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    context_object_name = 'empleado'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('persona_app:empleados_admin'))
