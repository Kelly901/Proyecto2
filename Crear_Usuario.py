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
				#Se comparan que la contraseña coincida con comparar contraseña
			elif contraseña!= confir_contraseña:
				 	print("Ingrese otra contraseña")
				 	print(nombre_usuario)

				 	return False

				 	
		self.usuario.append(Usuario(self.contador,nombre,apellido,nombre_usuario,contraseña,confir_contraseña))
		self.contador += 1
		return True

	def listar(self):
		print('id: \t nombre: \t Nombre de usuario: ')
		for us in self.usuario:

			print(str(us.ids)+ '\t' + us.nombre + '\t\t' + us.nombre_usuario)	



