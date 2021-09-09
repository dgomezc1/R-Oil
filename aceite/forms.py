from django.core.exceptions import ValidationError
from estudiante import forms
from django import forms
import estudiante
from usuario.models import User
from .models import registro_aceite
from estudiante.models import Estudiante

class FormularioAceite(forms.Form):
    ni = forms.IntegerField(label='numero identificacion',required=True,
    widget=forms.NumberInput(attrs={'placeholder':'Ingrese numero identificacion...'}))
    username = forms.CharField(label='username', required= True, widget=forms.TextInput(
        attrs= {'placeholder':'Ingrese nombre de usuario...'}
    ))
    
    cantidad_aceite=forms.IntegerField(label='cantidad aceite', required=True,widget=forms.NumberInput
    (attrs={'placeholder':'Ingrese cantidad de aceite...'}))
    nombre = forms.CharField(label='Nombre', required = True, widget=forms.TextInput(
        attrs={'placeholder':'Ingrese nombre...'}
    ) )

    def clean_username(self):
        nombre = self.cleaned_data["username"]
        ni1 = self.cleaned_data['ni']
        if not User.objects.filter(username = nombre).exists():
            raise forms.ValidationError('Este usuario no existe')
        elif not (User.objects.filter(username = nombre, ni=ni1).exists()):
            raise forms.ValidationError('La identificacion no corresponde con el nombre')
        elif not (Estudiante.objects.filter(user = User.objects.get(username = nombre))):
            raise forms.ValidationError('Este usuario no es un estudiante')
        return nombre

    def crear_registro(self, estudiante):
        
        registro = {
            'estudiante': estudiante, 
            'cantidad_aceite': self.cleaned_data['cantidad_aceite'],
            'nombre': self.cleaned_data['nombre'],
        }
        registro1 = registro_aceite.objects.create(**registro)


