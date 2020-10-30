from Usuario import Usuario
class Autenticacion:
	usuario=[]
	def __init__(self):
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

				 	return

		if nombre_usuario=="admin":
			tipo="admin"
			self.usuario.append(Usuario(self.contador,nombre,apellido,nombre_usuario,contraseña,confir_contraseña,tipo))
			self.contador += 1
		else:
			self.usuario.append(Usuario(self.contador,nombre,apellido,nombre_usuario,contraseña,confir_contraseña,"cliente"))
			self.contador += 1
				 				 	
		
		return True

	#Lisar
	def listar(self):
		print('id: \t nombre: \t Nombre de usuario: ')
		for us in self.usuario:

			print(str(us.ids)+ '\t' + us.nombre + '\t\t' + us.nombre_usuario +'\t\t\t'+us.tipo)	

	#Esto es de autenticar 
	def autenticar(self,nombre,password):
		for uss in Autenticacion.usuario:
			
			if uss.nombre_usuario== nombre and uss.contraseña== password:
				print("La Autenticacion es correcta")
				return True
			

		return False
   #Recupera contraseña
	def reucuperar_contrasena(self,nombre_usuario):
		for uss in Autenticacion.usuario:
			if uss.nombre_usuario==nombre_usuario:
				print(uss.contraseña)
				return True
		return False		
	#Dump para recuperrar la contraseña
	def dump3(self,nombre_usuario):
		for recorrer in self.usuario:
			if nombre_usuario ==recorrer.nombre_usuario:
				return{
					'contrasena':recorrer.contraseña,
					'estado': '1'
				}
		return False		
	#dump del los datos registrados
	def dump2(self,nombre,apellido,nombreUsuario,contrasena,confir_contrasena):
		for uu in self.usuario:
			if nombreUsuario == uu.nombre_usuario:
				return {
					'id':self.contador,
					'nombre':nombre,
					'apellido':apellido,
					'usuario':nombreUsuario,
					'contrasena':contrasena,
					'confirmar_password':confir_contrasena,
					'estado': '1'
					}

					#dump de los datos del usuario
	def dump(self,nombreU):
		
		for us in self.usuario:
			if nombreU==us.nombre_usuario:
				print(us.nombre_usuario)
				return{
					'id': us.ids,
					'nombre':us.nombre,
					'estado': '1',
					'tipo':us.tipo
				}
		return False			
