from django import forms
from django.forms import widgets
from .models import Institucion

class FormularioInstitucion(forms.ModelForm):
    class Meta:
        model =  Institucion
        fields = ('nombre', 'localidad', 'barrio', 'sede')
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'localidad': forms.TextInput(attrs={'placeholder': 'Municipio'}),
            'barrio': forms.TextInput(attrs={'placeholder': 'Barrio'}),
            'sede': forms.TextInput(attrs={'placeholder': 'Sede', 'required':False}),
        }