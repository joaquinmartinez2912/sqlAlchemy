import requests
from flask import Flask, flash, render_template, request, redirect, url_for
app = Flask(__name__)


BASE_URL = "https://apis.datos.gob.ar/georef/api/"

@app.route('/', methods =['post','get'])
def index():
    if request.method == "post":
        print(request.form)
    else:
        print("Hice una peticion GET")
    return render_template("index.html")

@app.route('/login', methods=['post'])
def login():
    usuario = request.form['usuario']
    password = request.form['password']
    tipo_usuario = request.form['tipo_usuario']
    if tipo_usuario =="0":
        tipo_usuario="Docente"
    if tipo_usuario=="1":
        tipo_usuario="Alumno"
    else:
        tipo_usuario="Administracion"
    return(f"<h1>aprete el boton y recibi el usuario:  {usuario},"
            f" y la contraseña:  {password},"
            f" el tipo de usuario es: {tipo_usuario}.</h1>"
    )
    

@app.route('/provincias')
def obtener_todas_provincias():
    response = requests.get(f"{BASE_URL}provincias")
    data = response.json()
    cantidad = data.get("cantidad")
    provincias =data.get("provincias")
    #print("provincias::",provincias.json())
    return render_template("provincias.html", cant_prov = cantidad, provs = provincias) # Esto es consumir los datos.

@app.route("/provincias/<id>/municipios")
def municipios_por_provincia(id):
    response = requests.get(f"https://apis.datos.gob.ar/georef/api/localidades?provincia={id}")
    data = response.json()
    municipios = data.get("localidades")
    return render_template("municipios.html", munis = municipios) # Esto es consumir los datos.


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/pruebaform")
def pruebaform():
    return render_template("pruebaform.html", nombre= request.args["code"])
