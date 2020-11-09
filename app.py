from flask import Flask,request,jsonify
from Autenticacion import Autenticacion
from AutenticacioJuego import AutenticacionJuego
from Juego import Juego
from Usuario import Usuario
import json
from flask_cors import CORS
from datetime import datetime
from GuardarComentarios import GuardarComentarios
from GuardarEnBiblioteca import GuardarEnBiblioteca
from GuardarGenero import GuardarGenero
app = Flask(__name__)
CORS(app)

miUsuario=[]

us=Autenticacion()
us.crearUsuario("Usuario","Maestro","admin","admin","admin")


us.listar()

var=AutenticacionJuego()
con=GuardarComentarios()
con.mostrar()
#Guarda en la biblioteca
biblio=GuardarEnBiblioteca()
#Guardar Genero
guardarG=GuardarGenero()

@app.route('/login',methods=['POST'])
def login():
	global miUsuario

	nombre=request.json['nombre_usuario']
	password=request.json['pasw_usuario']
	
	if us.autenticar(nombre,password)==True:
		print("correcta")
		return us.dump(nombre) 
	
			
	return {
			'id': '',
			'nombre':'',
			'estado': '0',
			
		}	
	
	
@app.route("/registrarse",methods=['POST'])
def registrarse():
	nombre1=request.json['nombre']
	apellido=request.json['apellido']
	nombreUsuario=request.json['usuario']
	contrasena=request.json['password']
	confirmarPassword=request.json['confirmar_password']	

	if us.crearUsuario(nombre1,apellido,nombreUsuario,contrasena,confirmarPassword)==True:

		return us.dump2(nombre1,apellido,nombreUsuario,contrasena,confirmarPassword)

	return {
		'id':'',
		'nombre':'',
		'apellido':'',
		'usuario':'',
		'contrasena':'',
		'confirmar_password':'',
		'estado': '0'
	}
#Metodo para crear Usuarios
@app.route("/crear_usuario",methods=['POST'])
def crear_usuario():
	nombre1=request.json['nombre']
	apellido=request.json['apellido']
	nombreUsuario=request.json['usuario']
	contrasena=request.json['password']
	confirmarPassword=request.json['confirmar_password']	

	if us.crearUsuario2(nombre1,apellido,nombreUsuario,contrasena,confirmarPassword)==True:

		return us.dump2(nombre1,apellido,nombreUsuario,contrasena,confirmarPassword)

	return {
		'id':'',
		'nombre':'',
		'apellido':'',
		'usuario':'',
		'contrasena':'',
		'confirmar_password':'',
		'estado': '0'
	}
#Metodo para recuperar contraseña
@app.route("/recuperacion",methods=['POST'])
def recuperacion():
	nombre=request.json['nombre_usuario']
	if us.reucuperar_contrasena(nombre)==True:
		print("correcta")
		return us.dump3(nombre) 
	
			
	return {
			'id': '',
			'nombre':'',
			'contrasena':'',
			'estado': '0'
		}
#Metodo para mostrar imagen		
@app.route("/imagen",methods=['GET'])
def imagen():
	misJuegos=[]

	for ju in AutenticacionJuego.juego:

		miJuego={
				'id':ju.id,
				'nombre':ju.nombre,
				'anio':ju.anio,
				'precio': ju.precio,
				'categoria1':ju.categoria1,
				'categoria2':ju.categoria2,
				'categoria3':ju.categoria3,
				'foto' :ju.foto,
				'banner' :ju.banner,
				'descripcion' :ju.descripcion
				}	
		misJuegos.append(miJuego)
	juego=jsonify(misJuegos)	
	return juego
#Metodo para mostar cliente
@app.route("/mostrarClientes",methods=['GET'])
def mostrarClientes():
	clientes=[]
	for u in Autenticacion.usuario:
		cliente={
				'id':u.ids,
				'nombre':u.nombre,
				'apellido':u.apellido,
				'usuario':u.nombre_usuario,
				'contrasena':u.contraseña,
				'confirmar_password':u.confir_contraseña,
				'estado': '1'
				}
		clientes.append(cliente)
	clien=jsonify(clientes)
	return clien			


		
@app.route("/modificarUsuario",methods=['POST'])
def modificarUsuario():
	id=request.json['id']
	nombre=request.json['nombre']
	apellido=request.json['apellido']
	usuario=request.json['usuario']
	contrasena=request.json['contrasena']
	
	
	if us.modificar_U(str(id),nombre,apellido,usuario,contrasena)==True:
		return {
			'estado': '1'
		}
	return {
			'id': '',
			'nombre':'',
			'contrasena':'',
			'estado': '0'
		}	

@app.route("/cargaMasiva",methods=['POST'])
def cargaMasiva():
	contenido=request.json['contenido']
	var.descomponer(contenido)
	return "1"
@app.route("/mostrarPerfil",methods=['POST'])
def mostrarPerfil():
	id=request.json['id']
	
	return us.dumpP(id)
		
		

	
#modificar perfil
@app.route("/modficarPerfil",methods=['POST'])
def modficarPerfil():
	id=request.json['id']
	nombre=request.json['nombre']
	apellido=request.json['apellido']
	usuario=request.json['usuario']
	contrasena=request.json['contrasena']
	confirmar_contrasena=request.json['confirmar_contrasena']
	if us.modificar(id,nombre,apellido,usuario,contrasena,confirmar_contrasena)==True:
		return us.dumpP(id)
	return{
			'id':'',
			'nombre':'',
			'contrasena':'',
			'estado': '0'
	}	
#Metodo para mostrar juego
@app.route("/mostrarJuego",methods=['POST'])
def mostrarJuego():
	id=request.json['id']

	return var.dump(id)

#Metodo para crear comentarios
@app.route("/crearComentarios",methods=['POST'])
def crearComentarios():	
	id=request.json['id']
	idU=request.json['idU']
	comentario=request.json['comentario']

	fecha= datetime.now()

	if con.crearComentario(id,idU,comentario,fecha)==True:
		return	con.dump1(id,idU,comentario,fecha)

	return {
			'id':'',
			'comentario':'',
			'fecha':''
	}

#Metodo para mostrar comentarios
@app.route("/mostrarComentarios",methods=['GET'])
def mostrarComentarios():
	comentarios=[]
	for u in GuardarComentarios.comentario:

		comentario={
				'id':u.id,
				'comentario':u.comentario,
				'fecha':u.fecha
				}
		comentarios.append(comentario)
	
	coment=jsonify(comentarios)
	return coment			
#Obtener el nombre de usuario del comentario
@app.route("/nombreComentario",methods=['POST'])
def nombreComentario():
	comentarios=[]
	id =request.json['id']
	idU =request.json['idU']
	return us.dumpP(str(idU))
#a
@app.route("/mostrarComentario",methods=['POST'])
def mostrarComentario():
	id =request.json['id']
	comentarios=[]
	for u in GuardarComentarios.comentario:
		comentario={
				'id':u.id,
				'idU':us.dumpNombre(str(u.idU)),	
				'comentario':u.comentario,
				'fecha':u.fecha
				}
		comentarios.append(comentario)
	
	coment=jsonify(comentarios)
		
	return coment

@app.route("/agregarAbiblioteca",methods=['POST'])
def agregarAbiblioteca():
	idU =request.json['idU']
	idJ =request.json['idJ']

	if biblio.guardarEnBiblioteca(idU,idJ):
		return biblio.dumpB()
	return "no"	
#Mostrar juegos adquiridos por el cliente
@app.route("/mostrarBibloteca",methods=['GET'])
def mostrarBiblioteca():

	biblioteca=[]
	for u in GuardarEnBiblioteca.biblioteca:
		biblio={
				'id':u.id,
				'idU':u.idU,
				'nombre': var.nombreJuego(str(u.idJ)),
				'foto':var.fotoJuego(str(u.idJ))
				
				}
		biblioteca.append(biblio)
	
	bibl=jsonify(biblioteca)
		
	return bibl
#agregar a opciones
@app.route("/mostrarOpcion",methods=['GET'])
def mostrarOpcion():
	for g in AutenticacionJuego.juego:
		guardarG.guardarGenero(g.categoria1)
		guardarG.guardarGenero(g.categoria2)
		guardarG.guardarGenero(g.categoria3)
	generos=[]
	for u in GuardarGenero.genero:
		genero={
				'genero':u.genero
				
				}
		generos.append(genero)
	
	gen=jsonify(generos)
		
	return gen
#Crear Juego

@app.route("/crearJuego",methods=['POST'])
def crearJuego():
	nombre =request.json['nombre']
	anio =request.json['anio']
	precio =request.json['precio']
	categoria1 =request.json['categoria1']
	categoria2 =request.json['categoria2']
	categoria3 =request.json['categoria3']
	foto =request.json['foto']
	banner=request.json['banner']
	descripcion =request.json['descripcion']
	if var.crearJuego2(nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion)==True:
		return var.dump2(nombre)
	return {
		'estado':'0'
	}
#mostrar juego
@app.route("/mostrarJuego2",methods=['GET'])
def mostrarJuego2():

	biblioteca=[]
	for u in AutenticacionJuego.juego:
		biblio={
				'id':u.id,
				'nombre':u.nombre,
				'anio':u.anio,
				'precio':u.precio,
				'categoria1':u.categoria1,
				'categoria2':u.categoria2,
				'categoria3':u.categoria3,
				'foto':u.foto,
				'banner':u.banner,
				'descripcion':u.descripcion
				
				}
		biblioteca.append(biblio)
	
	bibl=jsonify(biblioteca)
		
	return bibl	
#app
@app.route("/modificarJuego",methods=['POST'])	
def modificarJuegod():
	id=request.json['id']
	nombre =request.json['nombre']
	anio =request.json['anio']
	precio =request.json['precio']
	categoria1 =request.json['categoria1']
	categoria2 =request.json['categoria2']
	categoria3 =request.json['categoria3']
	foto =request.json['foto']
	banner=request.json['banner']
	descripcion =request.json['descripcion']



	if var.modificarJuego(id,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion)==True:

		return{
			'estado':'1'
		}
	return{
		'estado':'0'
	}	

#Eliminar
@app.route("/eliminar",methods=['POST'])	
def elminar():
	id=request.json['id']
	var.eliminar(int(id))

	return "1"

#Crear Pdf


#principal

@app.route("/")
def index():
	if var.dump(id)==True:
		return 
	return "En linea"

if __name__ == "__main__":
	app.run(threaded=True,port=9000,debug=True)

		
