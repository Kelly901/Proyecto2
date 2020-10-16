from Usuario import Usuario

class Crear_Usuario:
	def __init__(self):
		self.usuario = []
		self.contador = 0

	#Crear usuarios
	def crearUsuario(self,nombre,apellido,nombre_usuario,contraseña,confir_contraseña):

		for us in self.usuario:
			if us.nombre_usuario == nombre_usuario:
				print("El nombre de usuario ya esta repetido")
				return False

		self.usuario.append(Usuario(self.contador,nombre,apellido,nombre_usuario,contraseña,confir_contraseña))
		self.contador += 1
		return True

	def listar(self):
		print('id: \t nombre: \t Nombre de usuario: ')
		for us in self.usuario:

			print(str(us.ids)+ '\t' + us.nombre + '\t\t' + us.nombre_usuario)	


var_usuario= Crear_Usuario()			
var_usuario.crearUsuario("Diego","---","Squery","123","123")
var_usuario.crearUsuario("Diego","---","Squery2","123","123")
var_usuario.crearUsuario("Diego","---","Squery2","123","123")
var_usuario.listar()