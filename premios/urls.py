# Django
from django.urls import path

# Views
from premios.views import reclamarPremio, registroPremios, premiosDisponibles, premiosCanjeados


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
    path(
        route='canjeados/', 
        view= premiosCanjeados.as_view(),
        name='canjeados'
    ),
    path(
        route='reclamo/', 
        view=reclamarPremio.as_view(), 
        name="reclamo"
    ),
]