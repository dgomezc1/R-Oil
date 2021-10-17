import estudiante
from django.db import models
from instituciones.models import Institucion

from estudiante.models import Estudiante

# Create your models here.

class registro_aceite(models.Model):
    estudiante = models.ForeignKey(Estudiante, blank = False, null = False, on_delete = models.CASCADE)
    cantidad_aceite = models.IntegerField(blank = False, null = False)
    nombre = models.CharField(max_length=150, blank=False, null = False)
    institucion = models.ForeignKey(Institucion, blank = True, null = True, on_delete=models.SET_NULL)
    fecha = models.DateTimeField(auto_now_add=True)
