from django import forms
from django.contrib.auth.forms import AuthenticationForm

class FormularioUsuario(forms.Form):
    """ Formulario de registro base de datos
    Variables:
        password1
        password2: Verificacion contraseña
    """
    username = forms.CharField(label='username', required=True,max_length=50)
    nombre= forms.CharField(label="nombre", required=True, max_length=50)
    apellido = forms.CharField(label='apellidos', required=True)
    email = forms.EmailField(label="Email", required=True)
    ni = forms.IntegerField(label='numero identificacion',required=True)
    

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

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['type'] = 'text'
        #self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['type'] = 'password'
        #self.fields['password'].widget.attrs['placeholder']='Contraseña'