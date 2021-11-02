# Django
from django.urls import path

# Views
from premios.views import registroPremios, premiosDisponibles


urlpatterns = [
    path(
        route='registro/', 
        view= registroPremios.as_view(),
        name='registro_premio'
    ),
    path(
        route='disponibles/', 
        view= premiosDisponibles.as_view(),
        name='disponibles'
    ),
]