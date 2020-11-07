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

	#Crear usuario Administrador

	def crearUsuario2(self,nombre,apellido,nombre_usuario,contraseña,confir_contraseña):

		for us in self.usuario:

			if us.nombre_usuario == nombre_usuario:
				print("El nombre de usuario ya esta repetido")
				return False
				#Se comparan que la contraseña coincida con comparar contraseña
			elif contraseña!= confir_contraseña:
				 	print("Ingrese otra contraseña")
				 	print(nombre_usuario)

				 	return

		tipo="admin"
		self.usuario.append(Usuario(self.contador,nombre,apellido,nombre_usuario,contraseña,confir_contraseña,tipo))
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
	def comparar_nombre(self,nombre_usuario):
		for us in self.usuario:
			if us.nombre_usuario==nombre_usuario:
				print("no se pudo por el nombre de usuario")
				return "no"
		print("si se puede")		
		return "si"	

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
	def dump(self,nombre):
		
		for us in self.usuario:
			if nombre==us.nombre_usuario:
				print(us.nombre_usuario)
				return{
					'id': us.ids,
					'nombre':us.nombre,
					'estado': '1',
					'tipo':us.tipo

				}
		return False			

	def modificar_U(self,ids,nombre,apellido,nombre_usuario,contrasena):
		for us in self.usuario:
			if self.comparar_nombre(nombre_usuario)=="si":
				if str(us.ids) ==ids :
					us.nombre=nombre
					us.apellido=apellido
					us.nombre_usuario=nombre_usuario
					us.contraseña=contrasena
					print("si se pudo")
					return True
				
		return False	

	#Modificar mi suario
	def modificar(self,ids,nombre,apellido,nombre_usuario,contrasena,confir_contrasena):
		for us in self.usuario:
			if self.comparar_nombre2(nombre_usuario,contrasena,confir_contrasena)=="si":
				if str(us.ids) ==ids :
					us.nombre=nombre
					us.apellido=apellido
					us.nombre_usuario=nombre_usuario
					us.contraseña=contrasena
					print("si se pudo")
					return True
				
		return False	
	
	def comparar_nombre2(self,nombre_usuario,contrasena,confir_contrasena):
		for us in self.usuario:
			
			if us.nombre_usuario==nombre_usuario :
				print("no se pudo por el nombre de usuario")
				return "no"	
			if contrasena!= confir_contrasena:
				return "no"
			print("no se pudo por la contraseña")	
			
		print("si se puede")		
		return "si"		
	def comparar_contrasena(self,contrasena,confir_contrasena):
		if contrasena==confir_contrasena:
			print("contraseñas iguales")
			return "yes"
		print("contraseñas no iguales")	
		return "no"	

	def dumpP(self,id):
		
		for us in self.usuario:
			if str(us.ids)==id:
				print(us.nombre_usuario)
				return{
					'id': us.ids,
					'nombre':us.nombre,
					'apellido':us.apellido,
					'usuario':us.nombre_usuario,
					'contrasena':us.contraseña,
					'estado': '1',
					'tipo':us.tipo

				}
		return False
	def dumpNombre(self,id):
		
		for us in self.usuario:
			if str(us.ids)==id:
				print(us.nombre_usuario)
				return us.nombre_usuario
		return False	