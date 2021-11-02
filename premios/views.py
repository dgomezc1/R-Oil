# Django
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from usuario.models import User
from docente.models import Docente
from gestores.models import Gestores
from premios.models import Premio

# Forms
from premios.forms import FormularioPremio

# Mixins
from usuario.mixins import permisos_estudiante_aceite

# Create your views here.

class registroPremios(LoginRequiredMixin,permisos_estudiante_aceite, View):
    form_class = FormularioPremio
    template_name = 'premios/registro.html'

    def get(self, request, *args, **kwargs):
        form = FormularioPremio
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            institucion = None
            if request.user.admin_docente:
                docente = User.objects.get(username = request.user)
                institucion  =  (Docente.objects.get(user = docente)).institucion
            else:
                docente = User.objects.get(username = request.user)
                institucion  =  (Gestores.objects.get(user = docente)).institucion
            form.save(institucion)
        else:
            return render(request, self.template_name, {'form':form})

class premiosDisponibles(ListView, LoginRequiredMixin):
    model = Premio
    template_name = 'premios/disponibles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        return context

    def post(self, request, *args, **kwargs):
        print()