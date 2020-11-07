class Juego:

	def __init__(self,id,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):
		self.id=id
		self.nombre=nombre
		self.anio=anio
		self.precio=precio
		self.categoria1=categoria1
		self.categoria2=categoria2
		self.categoria3=categoria3
		self.foto=foto
		self.banner=banner
		self.descripcion=descripcion

	def dump(self):
		
		return {
				'id':ju.id,
				'nombre':ju.nombre,
				'anio':ju.anio,
				'precio': ju.precio,
				'categoria1':ju.categoria1,
				'categoria2':ju.categoria2,
				'categoria3':ju.categoria3,
				'foto' :ju.foto,
				'banner' :ju.banner,
				'descripcion' :ju.descripcion
			}
        		
     			 
