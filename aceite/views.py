import estudiante
from aceite.models import registro_aceite
from django.db.models.fields import mixins
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import FormularioAceite
from django.views.generic.edit import CreateView
from usuario.models import User
from estudiante.models import Estudiante
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import registro_aceite
from django.views import View
from usuario.mixins import permisos_estudiante_aceite
# Create your views here.



def registro_de_aceite(request):
    form = FormularioAceite()
    if request.method=='POST':
        form = FormularioAceite(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data['username']
            estudiante = User.objects.get(username = nombre)
            print(estudiante)
            estudiante1=Estudiante.objects.get(user=estudiante)
            form.crear_registro(estudiante1)
            return HttpResponse("El registro de aceite se hizo de manera correcta")
        else:
            return render(request,'registro_Aceite.html' ,{'form':form})
    return render(request,'registro_Aceite.html' ,{'form':form})

class registro_de_aceite2(permisos_estudiante_aceite, View):
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
            print(estudiante)
            estudiante1=Estudiante.objects.get(user=estudiante)
            form.crear_registro(estudiante1)
            return HttpResponse("Envio correcto de datos")

        return render(request, self.template_name, {'form':form})