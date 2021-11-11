# Django
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import management
from django.contrib import messages
from django.views import View

# Models
from instituciones.models import Institucion

# Forms
from instituciones.forms import FormularioInstitucion

# Mixins
from usuario.mixins import permisos_institucion_docentes

# Create your views here.

class registro_institucion(LoginRequiredMixin,permisos_institucion_docentes,CreateView):
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

class eliminacion_institucion(LoginRequiredMixin,permisos_institucion_docentes,View):
    template_name = "eliminacion/eliminacion_inst.html"

    def get_context_data(self, **kwargs):
        contex =  super().get_context_data(**kwargs)
        contex['lista'] = op_insituticion = Institucion.objects.all()
        return contex

    def get(self, request, *args, **kwargs):
        op_institucion = Institucion.objects.all()
        return render(request, self.template_name, {'lista': op_institucion})

    def post(self, request, *args, **kwargs):
        op_institucion = Institucion.objects.all()
        if request.user.admin_proyecto:
            Institucion.objects.get(nombre= request.POST.get("state")).delete()
            messages.success(request, "Eliminacion de institucion exitosa")
            return render(request, self.template_name, {'lista': op_institucion})
        else:
            messages.error(request, "No tiene los permisos necesarios")
            return render(request, self.template_name, {'lista': op_institucion})