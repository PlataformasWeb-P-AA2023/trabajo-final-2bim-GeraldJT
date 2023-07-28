from django.contrib.auth.models import User, Group
from locales.models import *

from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__' 
 
class LocalComidaSerializer(serializers.HyperlinkedModelSerializer):
    barrio_str = serializers.StringRelatedField(source="barrio", read_only=True)
    propietario_str = serializers.StringRelatedField(source="propietario", read_only=True)
    class Meta:
        model = LocalComida
        fields = '__all__' 

class LocalRepuestosSerializer(serializers.HyperlinkedModelSerializer):
    barrio_str = serializers.StringRelatedField(source="barrio", read_only=True)
    propietario_str = serializers.StringRelatedField(source="propietario", read_only=True)
    class Meta:
        model = LocalRepuestos
        fields = '__all__' 

