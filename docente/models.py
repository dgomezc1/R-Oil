from django.db import models
from instituciones.models import Institucion
from usuario.models import User

# Create your models here.
class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ni = models.BigIntegerField('numero_identificacion', unique=True,blank=True, null=True)
    institucion = models.ForeignKey(Institucion, blank = True, null = True, on_delete=models.CASCADE)
    telefono = models.IntegerField('telefono', null=False, blank=False)

    def getInstitucion(self):
        return self.institucion

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
