from django import forms
from django.forms import widgets
from .models import Institucion
import re

class FormularioInstitucion(forms.ModelForm):
    class Meta:
        model =  Institucion
        fields = ('nombre', 'localidad', 'barrio', 'sede')
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre...'}),
            'localidad': forms.TextInput(attrs={'placeholder': 'Ingrese el municipio...'}),
            'barrio': forms.TextInput(attrs={'placeholder': 'Ingrese el barrio...'}),
            'sede': forms.TextInput(attrs={'placeholder': 'Ingrese la sede...', 'required':False}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if bool(re.search(r'\d', nombre)):
            raise forms.ValidationError('El nombre contiene caracteres invalidos')
        return nombre

    def clean_localidad(self):
        localidad = self.cleaned_data.get('localidad')
        if bool(re.search(r'\d', localidad)):
            raise forms.ValidationError('El barrio contiene caracteres invalidos')
        return localidad