from django.db import models
from usuario.models import User

# Create your models here.
class Estudiante(models.Model):
    grado  = models.CharField('grado', max_length=10, null=False, blank=False)
    edad = models.IntegerField('edad', null=False, blank=False)
    barrio  = models.CharField('barrio', max_length=150, null=False, blank=False)
    telefono = models.IntegerField('telefono', null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aceite_recolectado = models.IntegerField('aceite recolectado', null=False, blank=False, default=0)
    puntos = models.IntegerField('puntos de recoleccion', null=False, blank=False, default=0)