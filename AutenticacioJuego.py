from Juego import Juego
import json
class AutenticacionJuego:
	juego=[]
	juego2=[]
	def __init__(self):
		self.contador=0

	def crearJuego(self,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):	

		self.juego.append(Juego(self.contador,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion))	
		self.contador+=1
		return True

	#Crear juego 2 para validar que el nombre no coincida
	def crearJuego2(self,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):	
		for ju in self.juego:
			if ju.nombre==nombre:

				print("El nombre esta repetido")
				return False	
		self.juego.append(Juego(self.contador,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion))	
		self.contador+=1
		return True	

	def mostrar(self):
		print('id: \t nombre \tcategoria1 \t categoria2 \t categoria3 \t descripcion')
		for ju in self.juego:
			print(str(ju.id )+'\t'+ju.nombre+'\t\t\t\t'+ju.precio+'\t\t'+ju.categoria1+'\t\t\t'+ju.categoria2+'\t\t\t\t'+ju.categoria3+'\t\t\t\t'+ju.descripcion)

	
	def descomponer(self,texto):
		
		texto2=texto.split("\n")
		for r in texto2:
			texto3=r.split(",")
			print(r.split(","))
			if texto[0]=="":
				return "no se puede"
			self.crearJuego(texto3[0],texto3[1],texto3[2],texto3[3],texto3[4],texto3[5],texto3[6],texto3[7],texto3[8])
		return texto

	def dump(self,id):
		for ju in self.juego:
			if str(ju.id)==id:
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
        	
		return False		 

	def dump2(self,nombre):
		for ju in self.juego:
			if ju.nombre==nombre:
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
					'descripcion' :ju.descripcion,
					'estado':'1'
				}
        	
		return False
	#Retornar imagen
	def nombreJuego(self,id):
		for ju in self.juego:
			if str(ju.id)==id:
				return ju.nombre
				
	

        	
		return False		

	#Retornar foto
	def fotoJuego(self,id):
		for ju in self.juego:
			if str(ju.id)==id:
				return ju.foto
				
			
        	
		return False	


	def bucarJuego(self,nombre):
		for j in self.juego:
			if j.nombre==nombre:
				print("El juego si existe")
				return True
		print("El juego no existe")		
		return False
	
	def modificarJuego(self,id,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):
		for us in self.juego:
			if self.comparar_nombre(nombre)=="si":
				if str(us.id) ==id:
					print(1)
					us.nombre=nombre
					us.anio=anio
					us.precio=precio
					us.categoria1=categoria1
					us.categoria2=categoria2
					us.categoria3=categoria3
					us.foto=foto
					us.banner=banner
					us.descripcion=descripcion
					print("si se pudo")
					return True

				
		return False	

	def comparar_nombre(self,nombre):
		for us in self.juego:
			if us.nombre==nombre:
				print("no se pudo por el nombre de usuario")
				return "no"
		print("si se puede")		
		return "si"

	def eliminar(self,id):
		self.juego.pop(id)	
		return True

