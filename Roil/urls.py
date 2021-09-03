"""Roil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from usuario.views import Login, logoutUsuario
#from student import views as student_views
from estudiante import views as estudiante_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('usuario.urls')),
    path('accounts/login/', Login.as_view(), name = "login"),
    path('logout/', login_required(logoutUsuario), name="logout"),

    #path('student/signup/', student_views.signup_view, name='student_signup'),

    path('estudiantes/', estudiante_views.signup_view, name='student_signup'),
    path('docentes/', include('docente.urls')),
    path('institucion/', include('instituciones.urls')),
]

