from django.contrib import admin
from .models import PerfilUsuario, RegistroConsumo

# Esto hace que aparezca la tabla de Usuarios
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'cedula', 'email') # Columnas que quieres ver

# Esto hace que aparezca la tabla de Consumos
@admin.register(RegistroConsumo)
class RegistroConsumoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_recurso', 'cantidad', 'fecha_consumo') # Columnas visibles
    list_filter = ('tipo_recurso', 'fecha_consumo') # Un panel lateral para filtrar rápido