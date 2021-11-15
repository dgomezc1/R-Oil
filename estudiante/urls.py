
# Django
from django.urls import path

# Views
from . import views


urlpatterns = [
    path('registro/', views.registro_estudiante.as_view(), name='registro de estudiante'),
    path('datos/', views.datos_estudiante.as_view(), name='datos' ),
]