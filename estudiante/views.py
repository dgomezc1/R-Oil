"""Student views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages

# Forms
from estudiante.forms import SignupForm, EstudianteForm

#Models
from instituciones.models import Institucion
from docente.models import Docente
from gestores.models import Gestores
from usuario.models import User

# Create your views here.
@login_required
def signup_view(request):
    """Sign up user view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            institucion = None
            if request.user.admin_docente:
                docente = User.objects.get(username = request.user)
                institucion  =  (Docente.objects.get(user = docente)).institucion
            else:
                docente = User.objects.get(username = request.user)
                institucion  =  (Gestores.objects.get(user = docente)).institucion
            form.save(institucion)
            return redirect('student_signup') 
    else: 
        form = SignupForm()

    return render(
        request=request, 
        template_name='estudiante/signup.html',
        context={
            'form': form
        }
    )

class registro_estudiante(LoginRequiredMixin, View):
    form_class = SignupForm()
    template_name = 'estudiante/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            institucion = None
            if request.user.admin_docente:
                docente = User.objects.get(username = request.user)
                institucion  =  (Docente.objects.get(user = docente)).institucion
            else:
                docente = User.objects.get(username = request.user)
                institucion  =  (Gestores.objects.get(user = docente)).institucion
            form.save(institucion)
            messages.success(request, "Registro de estudiante exitoso")
            return render(request, self.template_name, {'form':self.form_class})
        return render(request, self.template_name,{'form':form})