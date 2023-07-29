from flask import Flask, render_template, redirect, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

#Esoy poniendo un comentario
app = Flask(__name__)

#mysql+pymysql://usuario:contraseña@ip/nombre_db
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/alchemy"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 143.198.156.171
# BD2021itec

class Pais(db.Model):
    __tablename__ = "pais"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.name

class Provincia(db.Model):
    __tablename__ = "provincia"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(
        db.Integer,
        ForeignKey("pais.id"),
        nullable=False )

    def __str__(self):
        return self.name
    
class Localidad(db.Model):
    __tablename__ = "localidad"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia = db.Column(
        db.Integer,
        ForeignKey("provincia.id"),
        nullable=False )

    def __str__(self):
        return self.name
    
class Persona(db.Model):
    __tablename__ = "persona"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    tel = db.Column(db.String(100), nullable=False)
    domicilio = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    localidad = db.Column(
        db.Integer,
        ForeignKey("localidad.id"),
        nullable=False )
    is_active = db.Column(db.Boolean, nullable=False, default=False)

    def __str__(self):
        return self.name
    
@app.context_processor
def inject_paises():
    countries = db.session.query(Pais).all()   
    return dict(
        paises=countries
    )

@app.route("/")
def index():
    return render_template(
        "index.html"
    )

@app.route("/agregar_pais", methods=["POST"])
def nuevo_pais():
    if request.method=="POST":
        nombre_pais = request.form["nombre"]

        # Inicializo el objeto
        nuevi_pais = Pais(nombre=nombre_pais)
        # Preparo el objeto para enviarlo a la base de datos
        db.session.add(nuevi_pais)
        # Envio el objeto
        db.session.commit()

        return redirect(url_for("index"))


@app.route("/borrar_pais/<id>")
def borrar_pais(id):
    pais= Pais.query.get(id)
    db.session.delete(pais)
    db.session.commit()

    return redirect(url_for("index"))






#Query para obtener datos de la persona
""" personas = db.session.query(Persona).all()

if len(personas)>0:
    print("Hay personas")
else: 
    print ("No hay personas en DB") """
