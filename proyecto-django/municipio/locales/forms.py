from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from locales.models import *

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'cedula', 'correo']
        labels = {
            'nombres': _('Ingrese los nombres'),
            'apellidos': _('Ingrese los apellidos'),
            'cedula': _('Ingrese la cédula'),
            'correo': _('Ingrese el correo'),
        }

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombreBa', 'siglas']
        labels = {
            'nombreBa': _('Ingrese el nombre del barrio'),
            'siglas': _('Ingrese las siglas del barrio'),
        }
class LocalComidaForm(ModelForm):
    class Meta:
        model = LocalComida
        fields = ['direccion', 'tipoComida', 'ventasPMes', 'propietario', 'barrio']
        labels = {
            'direccion': _('Ingrese la direccion'),
            'tipoComida': _('Ingrese el tipo de comida'),
            'ventasPMes': _('Ingrese el valor de ventas proyectado'),
            'propietario': _('Seleccione el propietario'),
            'barrio': _('Seleccione el barrio'),
        }

class LocalRepuestosForm(ModelForm):
    class Meta:
        model = LocalRepuestos
        fields = ['direccion', 'valorTMercaderia', 'propietario', 'barrio']
        labels = {
            'direccion': _('Ingrese la direccion'),
            'valorTMercaderia': _('Ingrese el valor total de mercaderia'),
            'propietario': _('Seleccione el propietario'),
            'barrio': _('Seleccione el barrio'),
        }
