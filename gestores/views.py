# Django
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from usuario.models import User
from instituciones.models import Institucion

# Forms
from .forms import FormularioAdmin

# Mixins
from usuario.mixins import permisos_registro_admin

# Create your views here.

class registro_gestor(LoginRequiredMixin,permisos_registro_admin,CreateView):
    model = User
    form_class = FormularioAdmin
    template_name = 'gestores/registro_admin.html'

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
            return HttpResponse("Envio correcto de datos")
        else:
            return render(request, self.template_name, {'form':form, 'lista': op_institucion})
