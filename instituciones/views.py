# Django
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import management
from django.contrib import messages

# Models
from instituciones.models import Institucion

# Forms
from instituciones.forms import FormularioInstitucion

# Mixins
from usuario.mixins import permisos_institucion_docentes

# Create your views here.

class registro(LoginRequiredMixin,permisos_institucion_docentes,CreateView):
    model = Institucion
    form_class = FormularioInstitucion
    template_name = "registro_institucion.html"

    def post(self, request, *args, **kwargs):
        #management.call_command('runcrons')
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro de institucion exitoso")
            return render(request, self.template_name, {'form':FormularioInstitucion})
        else:
            return render(request, self.template_name, {'form':form})