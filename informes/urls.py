from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('global/', views.informe.as_view(), name="informe global"),
]