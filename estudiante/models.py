"""Student models."""

# Django
from django.db import models

# Models
from usuario.models import User
from instituciones.models import Institucion

# Create your models here.
class Estudiante(models.Model):
    """Estudiante model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ni = models.BigIntegerField('numero_identificacion', unique=True,blank=True, null=True)
    institucion = models.ForeignKey(Institucion, blank = True, null = True, on_delete=models.CASCADE)
    grado  = models.IntegerField('grado', null=False, blank=False)
    edad = models.IntegerField('edad', null=False, blank=False)
    barrio  = models.CharField('barrio', max_length=200, null=False, blank=False)
    telefono = models.IntegerField('telefono', null=False, blank=False)
    aceite_recolectado = models.IntegerField('aceite recolectado', null=False, blank=False, default=0)
    puntos = models.IntegerField('puntos de recoleccion', null=False, blank=False, default=0)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        
