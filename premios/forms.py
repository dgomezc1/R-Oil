
# Django
from django import forms
from django.contrib.auth.models import Group

# Models
from premios.models import Premio


class FormularioPremio(forms.Form):
    nombre = forms.CharField(label='nombre',required=True,
                            widget=forms.TextInput(attrs={'placeholder':'Ingrese el nombre del premio...'}))
    descripcion = forms.CharField(label='descripcion',required=True,
                            widget=forms.TextInput(attrs={'placeholder':'Ingrese la descripción del premio...'}))
    cantidad = forms.IntegerField(label='cantidad',required=True,
                            widget=forms.NumberInput(attrs={'placeholder':'Ingrese la cantidad de premios a registrar..'}))
    precio = forms.IntegerField(label='precio',required=True,
                            widget=forms.NumberInput(attrs={'placeholder':'Ingrese el costo del premio individual..'}))
    imagen = forms.ImageField(label='imagen')
    

    def save(self, institucion):
        data = self.cleaned_data
        datos = {
            'nombre': data['nombre'],
            'descripcion': data['descripcion'],
            'cantidad': data['cantidad'],
            'precio': data['precio'],
            'imagen': data['imagen'],
            'institucion_id': institucion
        }
        premio = Premio.objects.create(**datos)

