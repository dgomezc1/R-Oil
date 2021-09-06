from django.db.models.fields import mixins
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import FormularioDocente
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import CreateView
from usuario.models import User
from instituciones.models import Institucion
from django.contrib.auth.mixins import LoginRequiredMixin
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
            return HttpResponse("Envio correcto de datos")
        else:
            return render(request, self.template_name, {'form':form, 'lista': op_institucion})