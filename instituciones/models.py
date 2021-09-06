from django.db import models

# Create your models here.
class Institucion(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    localidad = models.CharField(max_length=150, null=False, blank=False,default='Medellin')
    barrio = models.CharField(max_length=150, null=False, blank=True)
    sede = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'