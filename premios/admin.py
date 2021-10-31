"""Premios admin classes."""

# Django
from django.contrib import admin

# Models
from premios.models import Premio, PremiosEntregados

# # Register your models here.
# @admin.register(Premio)
# class PremioAdmin(admin.ModelAdmin):
#     """Premio admin."""

#     list_display = ('pk', 'nombre', 'descripcion', 'cantidad', 'imagen',)
#     list_display_links = ('pk', 'nombre',)
#     list_editable = ('descripcion', 'cantidad',)

#     search_fields = ('nombre',)
#     list_filter = ('cantidad',)
admin.site.register(Premio)
admin.site.register(PremiosEntregados)