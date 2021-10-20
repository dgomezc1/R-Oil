from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.home.as_view(), name="home"),
    path('estudiante/', views.home_estudiante.as_view(), name="home_estudiante"),
]