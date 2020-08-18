from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaTextos'
    queryset = ['esto', 'es', 'una', 'prueba', 'de', 'listview']


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    # esto viene de nuestra base de datos
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    # son los atributos de mi objeto Prueba
    #fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    success_url = '/'
