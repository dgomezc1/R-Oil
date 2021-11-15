
# Django
from django.urls import path

# Views
from . import views


urlpatterns = [
    path('registro/', views.registro_docentes.as_view(), name='registro docente'),
]