from django.contrib import admin

# Importar las clases del modelo
from locales.models import *
class LocalComidaAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'tipoComida', 'ventasPMes', 'propietario', 'barrio')
    search_fields = ('propietario', 'tipoComida')
    raw_id_fields = ('barrio', 'propietario')
admin.site.register(LocalComida, LocalComidaAdmin)

class LocalRepuestosAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'valorTMercaderia', 'propietario', 'barrio')
    search_fields = ('propietario', 'direccion')
    raw_id_fields = ('barrio', 'propietario')

admin.site.register(LocalRepuestos, LocalRepuestosAdmin)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'correo')
    search_fields = ('cedula', 'correo')

admin.site.register(Persona, PersonaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombreBa', 'siglas')
    search_fields = ('nombreBa',)

admin.site.register(Barrio, BarrioAdmin)