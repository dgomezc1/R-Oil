from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from .forms import FormularioLogin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from usuario.mixins import permisos_estudiante_aceite

# Create your views here.

class home(LoginRequiredMixin,View):
    template_name = 'index1.html'
    redirect_field_name = 'estudiante'
    def get(self, request, *args, **kwargs):
        if request.user.admin_proyecto or request.user.admin_docente:           
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect(self.get_redirect_field_name())

class home_estudiante(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hola estudiante")

class Login(FormView):
    template_name = 'index.html'
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