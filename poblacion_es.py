import os
import time
import django
import random as rd
import poblacion_ace

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Roil.settings")
django.setup()

from estudiante.models import Estudiante
from instituciones.models import Institucion

instituciones = list(Institucion.objects.all())
nis = [1001, 1006, 1007, 1002]
barrios = ['Comuna 1','Comuna 2','Comuna 3','Comuna 4','Comuna 5','Comuna 6','Comuna 7','Comuna 8','Comuna 9','Comuna 10','Comuna 11','Comuna 12',
'Comuna 13','Comuna 14', 'Comuna 15', 'Comuna 16']

def generate_grado():
    return rd.randint(6,11)

def generate_ni():
    num = rd.randint(1, 2000000000)
    if num in nis:
        return generate_ni()
    else:
        nis.append(num)
        return num

def generate_telefono():
    return rd.randint(1, 4000000000)

def generate_estudiante(usuario, nombre):
    random_ni = generate_ni()
    random_institucion = rd.choice(instituciones)
    random_grado = generate_grado()
    random_edad = random_grado+6
    random_barrio = rd.choice(barrios)
    random_telefono = generate_telefono()
    estudiante = Estudiante.objects.create(user=usuario, ni = random_ni, institucion = random_institucion, grado = random_grado, edad=random_edad, barrio=random_barrio,telefono=random_telefono)
    for i in range(11):
        poblacion_ace.generate_registro(estudiante, random_institucion, nombre)
    #print(random_ni, random_institucion, random_grado, random_edad, random_barrio, random_telefono)