import django
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

# Create your views here.

def home(reques):
    return HttpResponse("Hola")

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