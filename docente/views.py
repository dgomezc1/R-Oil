
# Django
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Models
from usuario.models import User
from instituciones.models import Institucion

# Forms
from docente.forms import FormularioDocente

# Mixins
from usuario.mixins import permisos_institucion_docentes

# Create your views here.

class registro2(LoginRequiredMixin,permisos_institucion_docentes,CreateView):
    model = User
    form_class = FormularioDocente
    template_name = 'registro.html'

    def get_context_data(self, **kwargs):
        contex =  super().get_context_data(**kwargs)
        contex['lista'] = op_insituticion = Institucion.objects.all()
        return contex

    def post(self, request, *args, **kwargs) -> HttpResponse:
        op_institucion = Institucion.objects.all()
        form = self.form_class(request.POST)
        if form.is_valid():
            institucion = Institucion.objects.get(nombre= request.POST.get("state"))
            form.crear_usuario(institucion)
            messages.success(request, "Registro de docente exitoso")
            return render(request, self.template_name, {'form':FormularioDocente, 'lista': op_institucion})
        else:
            return render(request, self.template_name, {'form':form, 'lista': op_institucion})