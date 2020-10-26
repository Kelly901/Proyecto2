from flask import Flask, request, jsonify
from Autenticacion import Autenticacion
from flask_cors import CORS
app = Flask(__name__)

miUsuario=[]

miUsuario.append(Autenticacion(1,'user','123'))
miUsuario.append(Autenticacion(2,'user2','123'))
@app.route('/login',methods=['POST'])

def login():

	if request.method == 'POST':

		nombre=request.form.get('nombre_usuario')
		password=request.form.get('pasw_usuario')

		for user in miUsuario:

			if user.autenticar(nombre,password)==True:
			
				return user.dump() 
				

		return "hola"		
		
print(login)	
	

@app.route("/")
def index():
	nombre = miUsuario[0].usuario
	return nombre

if __name__ == "__main__":
	app.run(threaded=True,port=5000,debug=True)

		
