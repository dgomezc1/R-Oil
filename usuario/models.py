from django.db import models
from django.contrib.auth.models import AbstractUser
from instituciones.models import Institucion

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField('first name', max_length=150, blank=True, null=True)
    last_name = models.CharField('last name', max_length=150, blank=True, null=True)
    email = models.EmailField('email address', blank=False, null=False)    
    usuario_inst = models.BooleanField(default=False)
    admin_docente = models.BooleanField(default=False)
    admin_proyecto = models.BooleanField(default=False)

    def get_institucion(self):
        return self.institucion
    def get_usuario_inst(self):
        return self.usuario_inst
    def get_admin(self):
        return self.admin_proyecto

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'