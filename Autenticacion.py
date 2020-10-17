class Autenticacion:


	def __init__(self,id,usuario,password):
		self.id=id
		self.usuario=usuario
		self.password=password

	def autenticar(self,usuario,password):

		if self.usuario== usuario and self.password== password:
			print("La Autenticacion es correcta")
			return True
		print("La autenticacion fue incorrecta")
		return False
