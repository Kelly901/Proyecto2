from flask import Flask
from Autenticacion import Autenticacion
app = Flask(__name__)

miUsuario=[]

miUsuario.append(Autenticacion(1,'user','123'))

@app.route("/")
def index():
	nombre = miUsuario[0].usuario
	return nombre

if __name__ == "__main__":
	app.run(threaded=True,port=5000,debug=True)

		
