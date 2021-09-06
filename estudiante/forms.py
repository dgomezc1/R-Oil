"""Student forms."""

# Django 
from django import forms
from django.forms.widgets import TextInput

# Models
from usuario.models import User
from estudiante.models import Estudiante

class SignupForm(forms.Form):
    """Sign-up form."""

    # User data
    first_name = forms.CharField(max_length=150, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True) 

    ni = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    username = forms.CharField(min_length=4, max_length=50, widget=TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # Student data
    grado = forms.CharField(max_length=10, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    barrio = forms.CharField(max_length=200, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    telefono = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    # Validación especifica
    def clean_username(self):
        """Username must be unique."""
        # Los datos que ya limpio django por nosotros
        username = self.cleaned_data['username']
        # Usamos filter porque si usamos get y no existe, lanzaría una excepción
        # exist() solo para saber si existe (booleano)
        username_taken = User.objects.filter(username=username).exists() 
        if username_taken:
            # Django se encarga de subir la excepción hasta el html
            raise forms.ValidationError('Username is already in use.')
        return username # Es necesario que cuando se haga la validación de un campo, se regrese el campo

    # Validación especifica
    def clean_email(self):
        """Email must be unique."""
        # Los datos que ya limpio django por nosotros
        email = self.cleaned_data['email']
        # Usamos filter porque si usamos get y no existe, lanzaría una excepción
        # exist() solo para saber si existe (booleano)
        email_taken = User.objects.filter(email=email).exists() 
        if email_taken:
            # Django se encarga de subir la excepción hasta el html
            raise forms.ValidationError('Email is already in use.')
        return email # Es necesario que cuando se haga la validación de un campo, se regrese el campo

    # Validación final de todos los datos
    def clean(self):
        """Verify password confirmation match."""
        # Para no sobreescribir todo el metodo
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and student."""
        data = self.cleaned_data
        # Hay un dato que no nos sirve, que es password confirmation
        data.pop('password_confirmation')
        usuario = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'ni': data['ni'],
            'usuario_inst': True,
            'username': data['username'],
            'password': data['password'],
        }
        # Le enviamos todo el formulario
        user = User.objects.create(**usuario)

        estudiante = {
            'user': user,
            'grado': data['grado'],
            'edad': data['edad'],
            'barrio': data['barrio'],
            'telefono': data['telefono'],
        }
        estudiante = Estudiante.objects.create(**estudiante)

    
class EstudianteForm(forms.ModelForm):
    """Student form."""

    class Meta:
        """Form settings"""
        model = Estudiante
        fields = ('user', 'grado', 'edad', 'barrio', 'telefono')
    

