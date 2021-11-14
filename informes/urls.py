
# Django
from django.urls import path

# Views
from informes import views


urlpatterns = [
    path('global/', views.informeGlobal.as_view(), name="informe global"),
    path(
        route='local/', 
        view=views.informeLocal.as_view(),
        name='informe_local'
    )
]