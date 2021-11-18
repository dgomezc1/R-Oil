"""Premios models."""

# Django
from django.db import models

# Models
from estudiante.models import Estudiante
from instituciones.models import Institucion

# Create your models here.
class Premio(models.Model):
    """Model premio."""

    nombre  = models.CharField('nombre', max_length=45, null=False, blank=False)
    descripcion = models.TextField('descripcion', null=True, blank=True)
    cantidad  = models.IntegerField('cantidad', null=False, blank=False)
    precio = models.BigIntegerField('precio', null=False, blank=False)

    imagen = models.ImageField(
        upload_to='premios/pictures',
        null=True,
        blank=True
    )

    institucion_id = models.ForeignKey(Institucion, on_delete=models.CASCADE)

    entregados = models.ManyToManyField(Estudiante, through='PremiosEntregados')

    class Meta:
        verbose_name = 'Premio'
        verbose_name_plural = 'Premios'
        db_table = 'Premio'
        
class PremiosEntregados(models.Model):
    codigo_canjeo = models.CharField('codigo de canjeo', max_length=8, null=False, blank=False)
    fecha = models.DateField('fecha', auto_now_add=True, null=False, blank=False)
    estudiante_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    premio_id = models.ForeignKey(Premio, on_delete=models.CASCADE)
    entregado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Premios Entregados'
        verbose_name_plural = 'Premios Entregados'
        db_table = 'PremiosEntregados'