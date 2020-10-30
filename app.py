from flask import Flask,request,jsonify
from Autenticacion import Autenticacion
from Usuario import Usuario
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

miUsuario=[]

us=Autenticacion()
us.crearUsuario("Usuario","Maestro","admin","admin","admin")
us.crearUsuario("Kelly","km","s2","123","123")
us.crearUsuario("Susy","sus","Susy","123","123")
us.reucuperar_contrasena("Susy")
us.listar()
	
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

@app.route("/")
def index():
	
	return "En linea"

if __name__ == "__main__":
	app.run(threaded=True,port=9000,debug=True)

		
