from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.registro_estudiante.as_view(), name='registro de estudiante'),
]