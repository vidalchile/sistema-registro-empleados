from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return self.habilidad


class Empleado(models.Model):
    """ modelo para la tabla empleado """
    
    # Solo tendremos trabajos especificos
    # Contador
    # Administrador
    # Economista
    # Otro
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    firt_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre Completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    # creamos nuestra relación
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # relación mucho a mucho
    habilidades = models.ManyToManyField(Habilidades)
    #hoja_vidal = RichTextField()
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True, height_field=None, width_field=None, max_length=100)
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-firt_name']
        # validar que no exista una combinacion similar
        unique_together = ('firt_name', 'last_name')

    def __str__(self):
        return str(self.id) + ' - ' + self.firt_name + ' - ' + self.last_name