from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    #path('registro/', views.registro_de_aceite, name='registro de aceite'),
    path('registro/', views.registro_de_aceite2.as_view(), name='registro de aceite'),
]