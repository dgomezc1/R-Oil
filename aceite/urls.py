from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('registro/', views.registro_de_aceite.as_view(), name='registro de aceite'),
]