from django.urls import path
from django.urls.conf import include
from informes import informe


urlpatterns = [
    path('', views.informe.as_view(), name='informe'),
]