
# Django
from django.urls import path

# Views
from . import views


urlpatterns = [
    path('registroinst/', views.registro_institucion.as_view(), name='registro_institucion'),
    path('eliminacionInst/', views.eliminacion_institucion.as_view(), name="eliminacion_inst"),
]