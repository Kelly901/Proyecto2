from Comentarios import Comentarios
class GuardarComentarios:
	comentario=[]

	def crearComentario(self,id,idU,comentario,fecha):
		self.comentario.append(Comentarios(id,idU,comentario,fecha))	
		return True


	def mostrar(self):
		print('id: \t comentario \tfecha ')
		for ju in self.comentario:
			print(str(ju.id )+'\t'+ju.comentario+'\t\t\t\t'+ju.fecha)

	
	def dump1(self,id,idU,comentario,fecha):
		return {
				'id':id,
				'idU':idU,
				 'comentario':comentario,
				 'fecha':fecha
			}
        	
	def dump2(self,id):
		for ju in self.comentario:
			if id==str(ju.id):

				return True
		return False				



