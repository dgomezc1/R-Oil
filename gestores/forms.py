from django import forms
from .models import Gestores
from docente.models import Docente
from estudiante.models import Estudiante
from usuario.models import User
from django.contrib.auth.models import Group

class FormularioAdmin(forms.ModelForm):
    ni = forms.IntegerField(label='numero identificacion',required=True,
    widget=forms.NumberInput(attrs={'placeholder':'Ingrese numero identificacion..'}))
    telefono = forms.IntegerField(label='numero celular',required=True,
    widget=forms.NumberInput(attrs={'placeholder':'Ingrese numero de celular..'}))
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese contraseña...',
            'id':'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label='contraseña de confirmacion', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente la contraseña...',
            'id':'password2',
            'required':'required',
        }
    ))
    class Meta:
        model = User
        fields  = ('username', 'first_name', 'last_name', 'email')
        widgets = {'email':forms.EmailInput(
            attrs={'placeholder':'ingrese correo electronico...',
            }),
            'first_name':forms.TextInput(attrs={'placeholder':'ingrese nombre...'}),
            'last_name': forms.TextInput(attrs={'placeholder':'ingrese apellido...'}),
            'username': forms.TextInput(attrs={'placeholder':'ingrese nombre usuario...'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def clean_username(self):
        nombre = self.cleaned_data["username"]
        if User.objects.filter(username = nombre).exists():
            raise forms.ValidationError('El nombre de usuario no se encuentra disponible')
        return nombre

    def clean_email(self):
        emailu = self.cleaned_data["email"]
        if User.objects.filter(email = emailu).exists():
            raise forms.ValidationError('Este email ya ha sido utilizado')
        return emailu

    def clean_ni(self):
        ni_usuario = self.cleaned_data["ni"]
        if Docente.objects.filter(ni = ni_usuario).exists() or Estudiante.objects.filter(ni = ni_usuario).exists() or Gestores.objects.filter(ni = ni_usuario).exists():
            raise forms.ValidationError('El numero de identficacion no se encuentra disponible')
        return ni_usuario

    def clean_telefono(self):
        telefono = self.cleaned_data["telefono"]
        if telefono<2999999999 or telefono>3999999999:
            raise forms.ValidationError('El numero de celular no es valido')
        return telefono

    def crear_usuario(self, institucion):
        grupo = Group.objects.get(name = "admin")
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email']) 
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.admin_proyecto = True
        user.groups.add(grupo)
        user.set_password(self.cleaned_data['password1'])
        user.save()
        datos = {
            'user': user,
            'ni': self.cleaned_data['ni'],
            'institucion': institucion,
            'telefono': self.cleaned_data['telefono']
        }
        docente = Gestores.objects.create(**datos)

