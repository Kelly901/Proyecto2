from Biblioteca import Biblioteca
class GuardarEnBiblioteca:
	biblioteca=[]

	def __init__(self):
		self.contador=0

	def guardarEnBiblioteca(self,idU,idJ):
		self.biblioteca.append(Biblioteca(self.contador,idU,idJ))
		self.contador+=1
		return True

	def mostrar(self):
		for b in self.biblioteca:

			print("id:" +str(b.id)+" id Uusario: "+str(b.idU)+" id juego: "+str(b.idJ))	

	def dumpB(self):

		for b in self.biblioteca:

			return{
				'id':b.id,
				'idU':b.idU,
				'idJ':b.idJ
			}	
