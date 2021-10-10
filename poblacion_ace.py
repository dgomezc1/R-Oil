import os
import time
import django
import random as rd
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Roil.settings")
django.setup()

from estudiante.models import Estudiante
from instituciones.models import Institucion
from aceite.models import registro_aceite

def generate_aceite():
    return rd.randint(1,10)

def generate_dia():
    return rd.randint(1,27)

def generate_mes():
    return rd.randint(1,11)

def generate_registro(estudiante, institucion, nombre):
    random_cantidad = generate_aceite()
    random_fecha = datetime(2020, generate_mes(), generate_dia())
    registro_aceite.objects.create(estudiante=estudiante, cantidad_aceite = random_cantidad, nombre = nombre, institucion = institucion, fecha = random_fecha)