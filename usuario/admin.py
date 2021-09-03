from django.contrib import admin
from .models import User
from instituciones.models import Institucion

# Register your models here.
admin.site.register(User)
admin.site.register(Institucion)