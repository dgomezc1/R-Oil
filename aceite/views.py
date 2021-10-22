
# Django
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Models
from usuario.models import User
from estudiante.models import Estudiante
from docente.models import Docente
from gestores.models import Gestores

# Forms
from aceite.forms import FormularioAceite

# Mixins
from usuario.mixins import permisos_estudiante_aceite
# Create your views here.

class registro_de_aceite2(LoginRequiredMixin, permisos_estudiante_aceite, View):
    form_class  = FormularioAceite()
    template_name = 'registro_Aceite.html'

    def get(self, request, *args, **kwargs):
        form = FormularioAceite()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = FormularioAceite(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data['username']
            estudiante = User.objects.get(username = nombre)
            estudiante1=Estudiante.objects.get(user=estudiante)
            institucion = estudiante1.institucion
            institucionD = None
            if request.user.admin_docente:
                docente = User.objects.get(username = request.user)
                institucionD  =  (Docente.objects.get(user = docente)).institucion
            else:
                docente = User.objects.get(username = request.user)
                institucionD  =  (Gestores.objects.get(user = docente)).institucion
            if institucionD != institucion:
                error = "El estudiante no corresponde a su institucion"
                return render(request, self.template_name, {'form':form, 'error': error, 'act': True})
            else:
                form.crear_registro(estudiante1, institucion)
                return HttpResponse("Envio correcto de datos")

        return render(request, self.template_name, {'form':form})