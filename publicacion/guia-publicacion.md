# Paso 1:
Lo primero a realizar es la instalacion de la libreria de gunicorn 
# Paso 2: 
Entramos al archivo settings.py y agregamosel siguiente valor dentro de ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"] 
# Paso 3:
En el setting.py vamos a agregar lo siguiente STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
# Paso 4:
Nos dirigimos al archivo urls.py y vamos a importar from django.contrib.staticfiles.urls import staticfiles_urlpatterns y vamos agregar el siiguiente valor urlpatterns += staticfiles_urlpatterns() 
# Paso 5: 
vamos a ir a la consola y vamos a ejecutar el comando python manage.py collectstatic 
# Paso 6:
Para levantar el proyecto vamos a ejecutar el siguiente codigo: gunicorn --bind 0.0.0.0:8000 municipio.wsgi
# Paso 7:
Una vez que comprobamos que se ha podido subir la pagina de forma correcta vamos a ingresar en consola el comando: sudo nano /etc/systemd/system/
# Paso 8: 
Al momento de entrar el documento va a estar vacio, lo que vamos a hacer copiar y reemplazar los datos de las variables del siguiente codigo:

[Unit]
 metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
 usuario del sistema operativo que ejecutará el proceso
User=oem
 el grupo del sistema operativo que permite la comunicación a desde el servidor web-nginx con gunicorn. No se debe cambiar el valor
Group=www-data

 a través de la variable WorkingDirectory se indica la dirección absoluta del proyecto de Django
WorkingDirectory= /home/oem/Desktop/ejercicios/trabajo-final-2bim-GeraldJT/proyecto-django/municipio

 En Environment se indica el path de python
 Ejemplo 1: /usr/bin/python3.9
 Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entornos/entorno01/bin
Environment="/home/oem/entornos/entorno02/bin/"

 Detallar el comando para iniciar el servicio
ExecStart=/home/oem/entornos/entorno02/bin//gunicorn --workers 3 --bind unix:application.sock -m 007 municipio.wsgi:application

 Donde: aplicacion.sock es el nombre del archivo que se debe crear en el directorio del proyecto; proyectoDjango el nombre del proyecto que se intenta vincular con nginx.
 La expresión /bin/gunicorn no se debe modificar.

[Install]
 esta sección será usada para indicar que el servicio puede empezar cuando se inicie el sistema operativo. Se sugiere no cambiar el valor dado.
WantedBy=multi-user.target

# Paso 9:
vamos a iniciar el sistema a travez del comando: sudo systemctl start proyecto01

# Paso 10:
por medio del comando: sudo systemctl enable proyecto01 vamos a ver el status

# Paso 11:
verificamos que se haya creado el archivo application.pock

#Paso 12: se realiza la instalacion de nginx
