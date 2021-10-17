from django.urls import path
from django.urls.conf import include
from informes import views


urlpatterns = [
    path('global/', views.informeGlobal.as_view(), name="informe global"),
    path(
        route='local/', 
        view=views.informeLocal.as_view(),
        name='informe local'
    )
]