from django.core.exceptions import ValidationError
from estudiante import forms
from django import forms
import estudiante
from usuario.models import User
from .models import registro_aceite
from estudiante.models import Estudiante
from instituciones.models import Institucion

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
        elif not (Estudiante.objects.filter(user = User.objects.get(username = nombre))):
            raise forms.ValidationError('Este usuario no es un estudiante')
        elif not (Estudiante.objects.filter(user = User.objects.get(username = nombre), ni=ni1).exists()):
            raise forms.ValidationError('La identificacion no corresponde con el nombre')        
        return nombre

    def crear_registro(self, estudiante, institucion):
        estudiante.aceite_recolectado = estudiante.aceite_recolectado + self.cleaned_data['cantidad_aceite']
        estudiante.puntos = estudiante.puntos + self.cleaned_data['cantidad_aceite']
        estudiante.save()
        institucion.aceite_recolectado = institucion.aceite_recolectado + self.cleaned_data['cantidad_aceite']
        institucion.save()
        registro = {
            'estudiante': estudiante, 
            'cantidad_aceite': self.cleaned_data['cantidad_aceite'],
            'nombre': self.cleaned_data['nombre'],
            'institucion': institucion,
        }
        registro1 = registro_aceite.objects.create(**registro)


