from django import forms
from django.contrib.auth.forms import AuthenticationForm

from usuario.models import User
from docente.models import Docente
from estudiante.models import Estudiante

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['type'] = 'text'
        #self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['type'] = 'password'
        #self.fields['password'].widget.attrs['placeholder']='Contraseña'

class Formulario_eliminacion(forms.Form):
    ni = forms.IntegerField(label='numero identificacion',required=True,
    widget=forms.NumberInput(attrs={'placeholder':'Ingrese numero identificacion...'}))

    username = forms.CharField(label='username', required= True, widget=forms.TextInput(
        attrs= {'placeholder':'Ingrese nombre de usuario...'}
    ))

    def clean_username(self):
        nombre = self.cleaned_data["username"]
        ni1 = self.cleaned_data['ni']
        if not User.objects.filter(username = nombre).exists():
            raise forms.ValidationError('Este usuario no existe')
        elif not (Estudiante.objects.filter(user = User.objects.get(username = nombre)) or Docente.objects.filter(user = User.objects.get(username = nombre))):
            raise forms.ValidationError('Este usuario es un administrador')
        elif not (Estudiante.objects.filter(user = User.objects.get(username = nombre), ni=ni1).exists() or Docente.objects.filter(user = User.objects.get(username = nombre), ni=ni1).exists()):
            raise forms.ValidationError('La identificacion no corresponde con el nombre de usuario')        
        return nombre