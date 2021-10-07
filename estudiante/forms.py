"""Student forms."""

# Django 
from django import forms
from django.forms.widgets import TextInput

# Models
from usuario.models import User
from estudiante.models import Estudiante
from docente.models import Docente

class SignupForm(forms.Form):
    """Sign-up form."""

    # User data
    first_name = forms.CharField(max_length=150, required=True, widget=TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su nombre...'}))
    last_name = forms.CharField(max_length=150, required=True, widget=TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su apellido...'}))

    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su correo electronico...'})) 

    username = forms.CharField(min_length=4, max_length=50, widget=TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese un nombre de usuario...'}))

    password = forms.CharField(max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese una contraseña...'}))
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese nuevamente la contraseña...'}))

    # Student data
    ni = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control','placeholder':'Ingrese numero de identificacion...'}))
    grado = forms.CharField(max_length=10, required=True, widget=TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese el grado que se encuentra cursando...'}))
    edad = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control','placeholder':'Ingrese su edad...'}))
    barrio = forms.CharField(max_length=200, required=True, widget=TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese el barrio de residencia...'}))
    telefono = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control','placeholder':'Ingrese su numero de telefono...'}))
    

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
            raise forms.ValidationError('El nombre de usuario no se encuentra disponible.')
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
            raise forms.ValidationError('El email ya está en uso.')
        return email # Es necesario que cuando se haga la validación de un campo, se regrese el campo

    # Validación especifica
    def clean_ni(self):
        """ni must be unique."""
        # Los datos que ya limpio django por nosotros
        ni = self.cleaned_data['ni']
        # Usamos filter porque si usamos get y no existe, lanzaría una excepción
        # exist() solo para saber si existe (booleano)
        if Estudiante.objects.filter(ni=ni).exists() or Docente.objects.filter(ni=ni).exists() :
            # Django se encarga de subir la excepción hasta el html
            raise forms.ValidationError('El número de identificación ya está en uso.')
        return ni # Es necesario que cuando se haga la validación de un campo, se regrese el campo

    # Validación final de todos los datos
    def clean(self):
        """Verify password confirmation match."""
        # Para no sobreescribir todo el metodo
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('¡Las contraseñas no coinciden!')

        return data

    def save(self, Institucion):
        """Create user and student."""
        data = self.cleaned_data
        # Hay un dato que no nos sirve, que es password confirmation
        data.pop('password_confirmation')
        usuario = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'usuario_inst': True,
            'username': data['username'],
        }
        # Le enviamos todo el formulario

        user = User.objects.create(**usuario)
        print("Sin problemas")
        user.set_password(data['password'])
        user.save()

        estudiante = {
            'user': user,
            'ni': self.cleaned_data['ni'],
            'institucion': Institucion,
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
    

