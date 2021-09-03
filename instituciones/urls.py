from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('registroinst/', views.registro.as_view(), name='registro_institucion'),
]