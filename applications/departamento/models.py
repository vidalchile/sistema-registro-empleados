from django.db import models

# Create your models here.

class Departamento(models.Model):
    # no es necesario crear el ID
    name = models.CharField('Nombre', max_length=50, blank=True)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        # validar que no exista una combinacion similar
        unique_together = ('name', 'short_name')

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.short_name