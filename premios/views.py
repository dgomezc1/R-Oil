# Django
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse

# Models
from usuario.models import User
from docente.models import Docente
from gestores.models import Gestores
from premios.models import Premio, PremiosEntregados
from estudiante.models import Estudiante

# Forms
from premios.forms import FormularioPremio

# Mixins
from usuario.mixins import permisos_estudiante_aceite

# Python
import random

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

    def get_price_institution(request):
        usuario = User.objects.get(username = request.user)
        institucion  =  (Estudiante.objects.get(user = usuario)).institucion
        return Premio.objects.filter(institucion_id = institucion).exclude(cantidad = 0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        return context

    def get(self, request, *args, **kwargs):
        premios = premiosDisponibles.get_price_institution(request)
        usuario = User.objects.get(username = request.user)
        estudiante = Estudiante.objects.get(user = usuario)
        return render(request, self.template_name, {'premios': premios, 'puntos':estudiante.puntos})
        
    def post(self, request, *args, **kwargs):
        usuario = User.objects.get(username = request.user)
        estudiante = Estudiante.objects.get(user = usuario)
        premio = Premio.objects.get(id=request.POST["premio"])
        premio.cantidad = premio.cantidad -1
        premio.save()
        if(estudiante.puntos>=premio.precio):
            estudiante.puntos = estudiante.puntos -premio.precio
            estudiante.save()
            codigo = generar_codigo_canjeo()
            datos = {
                "codigo_canjeo": codigo,
                "estudiante_id":estudiante,
                "premio_id" : premio,
            }
            PremiosEntregados.objects.create(**datos)
            data = {
                "resultado":True,
                "codigo": "Codigo cangeo: "+codigo,
                "puntos": "Puntos disponibles: "+str(estudiante.puntos)
            }
        else:
            data = {
                "resultado":False,
            }
        return JsonResponse(data, safe = False)

class premiosCanjeados(ListView, LoginRequiredMixin):
    model = PremiosEntregados
    template_name = 'premios/canjeados.html'

    def get_premios_canjeados(request):
        usuario = User.objects.get(username = request.user)
        estudiante  =  Estudiante.objects.get(user = usuario)
        return PremiosEntregados.objects.filter(estudiante_id = estudiante)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        return context

    def get(self, request, *args, **kwargs):
        premios_canjeados = premiosCanjeados.get_premios_canjeados(request)
        usuario = User.objects.get(username = request.user)
        estudiante = Estudiante.objects.get(user = usuario)
        premios = Premio.objects.filter(institucion_id_id = estudiante.institucion)
        return render(
            request, 
            self.template_name, 
            {'premios_canjeados': premios_canjeados, 'puntos':estudiante.puntos, 'premios': premios,}
        )


def generar_codigo_canjeo():
    minus="abcdefghijklmnopqrstuvxyz"
    mayus=minus.upper()
    numeros="0123456789"

    base=minus+mayus+numeros

    muestra = random.sample(base, 8)
    codigo = "".join(muestra)
    return codigo