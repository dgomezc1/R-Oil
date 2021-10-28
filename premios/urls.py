# Django
from django.urls import path

# Views
from premios.views import registroPremios


urlpatterns = [
    path(
        route='registro/', 
        view= registroPremios.as_view(),
        name='registro_premio'
    ),
]