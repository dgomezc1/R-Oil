from django.contrib import admin
from .models import User
from instituciones.models import Institucion
from estudiante.models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    """Estudiante admin."""
    list_display = ('user', 'grado', 'edad', 'barrio', 'telefono', 'aceite_recolectado', 'puntos')
    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
    )
    readonly_fields = ('aceite_recolectado', 'puntos')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""
    list_display = ('username', 'first_name', 'last_name', 'email', 'ni', 'institucion', 'usuario_inst', 'docente', 'admin_proyecto')

# Register your models here.
@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    """Institucion admin."""
    list_display = ('nombre', 'localidad', 'barrio', 'sede')

