
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
from docente.models import Docente
from estudiante.models import Estudiante
from gestores.models import Gestores
from .models import User
from django.contrib import messages

# Forms
from usuario.forms import Formulario_eliminacion, FormularioLogin

# Models
from instituciones.models import Institucion
from usuario.mixins import permisos_estudiante_aceite
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
    template_name = 'home_estudiantes.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

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

class Eliminar_usuario(LoginRequiredMixin,permisos_estudiante_aceite,View):
    form = Formulario_eliminacion()
    template_name="eliminacion/eliminacion_usuario.html"

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name, {'form':self.form})

    def post(self, request, *args, **kwargs):
        form  = Formulario_eliminacion(request.POST)
        if form.is_valid():
            username_eliminado = form.cleaned_data['username']
            usuario_eliminado = User.objects.get(username = username_eliminado)
            if usuario_eliminado.usuario_inst:
                estudiante_eliminado = Estudiante.objects.get(user = usuario_eliminado)
                #Si es un docente el que va a eliminar
                if request.user.admin_docente:
                    docente = User.objects.get(username = request.user)
                    institucion_docente  =  (Docente.objects.get(user = docente)).institucion
                    if institucion_docente == estudiante_eliminado.institucion:
                        usuario_eliminado.delete()
                        messages.success(request, "El estudiante ha sido eliminado con exito")
                        return render(request, self.template_name, {'form':Formulario_eliminacion()})
                    else:
                        messages.error(request, "El estudiante no corresponde a su institucion")
                #Si es un administrador el que va a eliminar
                elif request.user.admin_proyecto:
                    usuario_eliminado.delete()
                    messages.success(request, "El estudiante ha sido eliminado con exito")
                    return render(request, self.template_name, {'form':Formulario_eliminacion()})
                else:
                    messages.error(request, "No cuenta con los permisos para eliminar usuarios")
            #Si vamos a eliminar un Docente o administrador
            else:
                if request.user.admin_proyecto:
                    User.objects.get(username = username_eliminado).delete()
                    messages.success(request, "Usuario eliminado con exito")
                    return render(request, self.template_name, {'form':Formulario_eliminacion()})
                else:
                    messages.error(request, "No cuenta con los permisos para eliminar docentes")
        return render(request, self.template_name, {'form':form})

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')