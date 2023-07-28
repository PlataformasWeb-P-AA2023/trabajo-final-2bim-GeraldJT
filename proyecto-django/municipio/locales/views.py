from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User, Group
from locales.serializers import BarrioSerializer, GroupSerializer, LocalComidaSerializer, LocalRepuestosSerializer, PersonaSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
# importar las clases de models.py
from locales.models import *

# importar los formularios de forms.py
from locales.forms import *
# Create your views here.
def index(request):

    localesC = LocalComida.objects.all()
    informacion_template = {'localC': localesC, 'numero_locales': len(localesC)}
    return render(request, 'indexC.html', informacion_template)

def indexR(request):

    localesR = LocalRepuestos.objects.all()
    informacion_template = {'localR': localesR, 'numero_locales': len(localesR)}
    return render(request, 'indexR.html', informacion_template)

def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)

#@login_required(login_url='/entrando/login/')
# @permission_required('administrativo.add_estudiante', )
#@permission_required('administrativo.add_estudiante', login_url="/entrando/login/")

#CRUD Local Comida

def crear_LocalComida(request):
    """
    """
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = LocalComidaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearLocalComida.html', diccionario)


#@login_required(login_url='/entrando/login/')
@permission_required('locales.change_localcomida', login_url="/entrando/login/")
def editar_LocalComida(request, id):
    """
    """
    localC = LocalComida.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST, instance=localC)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = LocalComidaForm(instance=localC)
    diccionario = {'formulario': formulario}

    return render(request, 'editarLocalComida.html', diccionario)

@permission_required('locales.delete_localcomida', login_url="/entrando/login/")
def eliminar_LocalComida(request, id):
    """
    """
    localC = LocalComida.objects.get(pk=id)
    localC.delete()
    return redirect(index)


# CRUD Local Repuestos

def crear_LocalRepuestos(request):
    """
    """
    if request.method=='POST':
        formulario = LocalRepuestosForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(indexR)
    else:
        formulario = LocalRepuestosForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearLocalRepuestos.html', diccionario)


#@login_required(login_url='/entrando/login/')
@permission_required('locales.editar_LocalRepuestos', login_url="/entrando/login/")
def editar_LocalRepuestos(request, id):
    """
    """
    localR = LocalRepuestos.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalRepuestosForm(request.POST, instance=localR)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexR)
    else:
        formulario = LocalRepuestosForm(instance=localR)
    diccionario = {'formulario': formulario}

    return render(request, 'editarLocalRepuestos.html', diccionario)

@permission_required('locales.eliminar_LocalRepuestos', login_url="/entrando/login/")
def eliminar_LocalRepuestos(request, id):
    """
    """
    localR = LocalRepuestos.objects.get(pk=id)
    localR.delete()
    return redirect(indexR)

# CRUD Persona

def crear_Persona(request):
    """
    """
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(lista_Persona)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearPersona.html', diccionario)


#@login_required(login_url='/entrando/login/')
def editar_Persona(request, id):
    """
    """
    personas = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=personas)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(lista_Persona)
    else:
        formulario = PersonaForm(instance=personas)
    diccionario = {'formulario': formulario}

    return render(request, 'editarPersona.html', diccionario)


def eliminar_Persona(request, id):
    """
    """
    personas = Persona.objects.get(pk=id)
    personas.delete()
    return redirect(lista_Persona)



# CRUD Barrio

def crear_Barrio(request):
    """
    """
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(lista_Barrio)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)


#@login_required(login_url='/entrando/login/')
def editar_Barrio(request, id):
    """
    """
    barrios = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrios)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(lista_Barrio)
    else:
        formulario = BarrioForm(instance=barrios)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)


def eliminar_Barrio(request, id):
    """
    """
    barrios = Barrio.objects.get(pk=id)
    barrios.delete()
    return redirect(lista_Barrio)

def lista_Barrio(request):

    barrios= Barrio.objects.all()
    diccionario = {'barrios': barrios, 'numero_barrios': len(barrios)}

    return render(request, 'listaBarrio.html', diccionario)

def lista_Persona(request):
    
    personas= Persona.objects.all()
    diccionario = {'personas': personas, 'numero_personas': len(personas)}

    return render(request, 'listaPersona.html', diccionario)

class UserViewSet(viewsets.ModelViewSet):
   
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
   
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonaViewSet(viewsets.ModelViewSet):
    
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]

class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer 
    permission_classes = [permissions.IsAuthenticated]


class LocalComidaViewSet(viewsets.ModelViewSet):
    queryset = LocalComida.objects.all()
    serializer_class = LocalComidaSerializer
    permission_classes = [permissions.IsAuthenticated]

class LocalRepuestosViewSet(viewsets.ModelViewSet):
    queryset = LocalRepuestos.objects.all()
    serializer_class = LocalRepuestosSerializer
    permission_classes = [permissions.IsAuthenticated]


