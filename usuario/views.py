
# Django
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib import messages

# Forms
from usuario.forms import FormularioLogin

# Models
from instituciones.models import Institucion
# Create your views here.

class home(LoginRequiredMixin,View):
    template_name = 'home_docentes.html'
    redirect_field_name = 'estudiante'
    def get(self, request, *args, **kwargs):
        if request.user.admin_proyecto or request.user.admin_docente:
            if request.user.admin_proyecto:
                insituciones = Institucion.objects.all()
                mensaje = False
                texto = ""
                for i in range(len(insituciones)):
                    if insituciones[i].aceite_recolectado > 100:
                        mensaje = True
                        texto = texto + "* "+insituciones[i].nombre+", "
                if mensaje:
                    messages.info(request, texto)          
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect(self.get_redirect_field_name())

class home_estudiante(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hola estudiante")

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')
 
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    #dispatch verifica la peticion si es GET o POST
    def dispatch(self, request, *args, **kwargs):
        #Si el usuario esta autentificado se lleva al reverse_lazy
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        #si no me tiene que mandar al login y llamo a dispatch y pinto el metodo qeu corresponte
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')