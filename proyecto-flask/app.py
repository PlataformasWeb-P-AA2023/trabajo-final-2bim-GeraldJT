from flask import Flask, render_template
import requests
import json
from config import usuario, clave

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/personas")
def las_personas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/personas/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("laspersonas.html", datos=datos,
    numeor=numero)


@app.route("/barrios")
def los_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrios/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("losbarrios.html", datos=datos,
    numero=numero)

@app.route("/localComida")
def los_losLocalesComida():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/localComida/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("localesComida.html", datos=datos,
    numero=numero)

@app.route("/localRepuestos")
def los_losLocalesRepuestos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/localRepuestos/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("localesRepuestos.html", datos=datos,
    numero=numero)



