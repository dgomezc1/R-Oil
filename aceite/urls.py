
# Django
from django.urls import path

# Views
from . import views


urlpatterns = [
    path('registro/', views.registro_de_aceite.as_view(), name='registro de aceite'),
]