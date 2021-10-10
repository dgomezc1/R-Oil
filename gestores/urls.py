from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('registro/', views.registro_gestor.as_view(), name='registro gestores'),
]