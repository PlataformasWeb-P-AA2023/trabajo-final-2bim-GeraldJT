"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('local/Comida', views.index, name='index'),
        path('local/Repuestos', views.indexR, name='indexR'),
        #Local Comida
        path('crear/LocalComida', views.crear_LocalComida,
            name='crear_LocalComida'),
        path('editar_localC/<int:id>', views.editar_LocalComida,
            name='editar_LocalComida'),
        path('eliminar/localC/<int:id>', views.eliminar_LocalComida,
            name='eliminar_LocalComida'),
        #Local Repuestos

        path('crear/LocalRepuesto', views.crear_LocalRepuestos,
            name='crear_LocalRepuestos'),
        path('editar_localRepuestos/<int:id>', views.editar_LocalRepuestos,
            name='editar_LocalRepuestos'),
        path('eliminar/localR/<int:id>', views.eliminar_LocalRepuestos,
            name='eliminar_LocalRepuestos'),
        
        #Persona
        path('listaPersona', views.lista_Persona,
            name='lista_Persona'),
        path('crear/Persona', views.crear_Persona,
            name='crear_Persona'),
        path('editar_Persona/<int:id>', views.editar_Persona,
            name='editar_Persona'),
        path('eliminar/persona/<int:id>', views.eliminar_Persona,
            name='eliminar_Persona'),
        
        #Barrio

        path('listaBarrio', views.lista_Barrio,
            name='lista_Barrio'),
        path('crear/Barrio', views.crear_Barrio,
            name='crear_Barrio'),
        path('editar_Barrio/<int:id>', views.editar_Barrio,
            name='editar_Barrio'),
        path('eliminar/Barrio/<int:id>', views.eliminar_Barrio,
            name='eliminar_Barrio'),
        ##
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
 ]
