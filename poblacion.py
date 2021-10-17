import os
import time
import django
import random as rd
import poblacion_es

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Roil.settings")
django.setup()

from usuario.models import User

vocals = ['a','e','i','o','u']  
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
                'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'] 
nombres = ['Jaime', 'Francisco', 'Andrea', 'Ruth', 'Silvana', 'Ariana', 'Luis', 'Felipe', 'Hansel', 'Andres', 'Aniyensy', 'Sarai', 'Karla', 'Paulette', 'Montserrat', 'Carolina', 'Lisset', 'Vianey',
'Jose', 'Ignacio', 'Cipriano', 'Ariel', 'Miguel', 'Alejandro', 'Danna', 'Veronica', 'Daniel', 'Fernando', 'Samanta', 'Julia', 'Irma', 'Esteban', 'David', 'Simon', 'Samuel', 'Santiago', 'Carlos', 'Andres', 'Gloria', 'Salome', 'Angela']
apellidos = ['Aguayo', 'Gonzalez', 'Chavez', 'Heredia', 'Cortes', 'Lagunes', 'Ramos', 'Delgado', 'Barron', 'Espejo', 'Flores', 'Aguilar','Silva','Garcia','Arreguin','Orozco','Gomez','Correa','Meneses','Diaz','Ortiz','Zapata','Espinosa','Jaramilo',
'Ochoa','Castaño','Vargas','Trejo','Guerrero','Padres','Paredes','Marin','Amaya','Llanos','Perez','Naranjo','Benjumea','Cardona','Cadavid','Elias','Castro','Chaverra','Nieto','Sanchez','Guarin','Guiral','Palacios','Arias','Herrera','Lara', 'Agapito']
correos = ['@outlook.com','@outlook.co', '@outlook.es','@gmail.com','@eafit.edu.co','@yahoo.com','@yahoo.es','@yahoo.co','@pildoras.com','@pildoras.es','@pildoras.co']

def generate_string(length):
    if length <=0:
        return False
    
    radom_string = ''

    for i in range(length):
        desicion = rd.choice(('vocals','consonants'))
        if radom_string[-1:].lower() in vocals:
            desicion = 'consonants'
        if radom_string[-1:].lower in consonants:
            desicion = 'vocals'

        if desicion == 'vocals':
            character = rd.choice(vocals)
        else:
            character = rd.choice(consonants)
        
        radom_string += character
    return radom_string

def generate_number():
    return rd.randint(4,9)

def generate_user(count):
    for j in range(count):
        length = generate_number()
        random_name = rd.choice(nombres)
        random_apellido = rd.choice(apellidos)+' '+rd.choice(apellidos)
        random_user_name = generate_string(length)
        random_email = random_user_name + rd.choice(correos)
        random_pass = generate_string((length*2))
        usuario = User.objects.create(username=random_user_name, first_name=random_name,last_name=random_apellido, email=random_email, usuario_inst=True)
        usuario.set_password(random_pass)
        usuario.save()
        print(random_name, random_apellido,random_user_name,random_pass,random_email)
        poblacion_es.generate_estudiante(usuario, random_name)

if __name__ == "__main__":
    generate_user(300)
    print("------------------------terminado-----------------")