from Categoria import Categoria
class GuardarGenero:

	genero=[]

	def guardarGenero(self,genero):

		for gen in self.genero:

			if gen.genero==genero:
				return False
		self.genero.append(Categoria(genero))
		return True 		

	def mostrar(self):
		for gen in self.genero:
			 print(gen.genero)	


