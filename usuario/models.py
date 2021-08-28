from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    localidad = models.CharField(max_length=150, null=False, blank=False)
    barrio = models.CharField(max_length=150, null=False, blank=True)
    sede = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    first_name = models.CharField('first name', max_length=150, blank=True, null=True)
    last_name = models.CharField('last name', max_length=150, blank=True, null=True)
    email = models.EmailField('email address', blank=False, null=False)
    institucion = models.ForeignKey(Institucion, blank = True, null = True, on_delete=models.CASCADE)
    ni = models.BigIntegerField('numero_identificacion', unique=True,blank=True, null=True)
    usuario_inst = models.BooleanField(default=False)

    def get_institucion(self):
        return self.institucion
    def get_usuario_inst(self):
        return self.usuario_inst

class Estudiante(models.Model):
    grado  = models.CharField('grado', max_length=10, null=False, blank=False)
    edad = models.IntegerField('edad', null=False, blank=False)
    barrio  = models.CharField('barrio', max_length=150, null=False, blank=False)
    telefono = models.IntegerField('telefono', null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aceite_recolectado = models.IntegerField('aceite recolectado', null=False, blank=False)
    puntos = models.IntegerField('puntos de recoleccion', null=False, blank=False)