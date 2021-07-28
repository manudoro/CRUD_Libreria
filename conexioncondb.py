"""En este módulo se realiza la interacción con la base de datos
del programa, a partir del paquete sqlite3."""
import sqlite3

class Crud:
	"""En la clase Crud están contenidos todos los metodos necesarios
	para inteactuar con la base de datos, ya sea para alta, baja,
	modificación o consulta"""
	def __init__(self):
		"""El metodo de iniciación realiza la conexión a la base de
		datos y contiene el atributo self.cursor que utilizaran los
		metodos restantes"""
		self.base = 'basededatos1.db'
		self.conexion = sqlite3.connect(self.base)
		self.cursor = self.conexion.cursor()

	def get_query(self, query, parametros=()):
		"""Este método sera llamado para ejecutar las acciones
		de alta, baja y modificación de registros."""
		self.cursor.execute(query,parametros)
		self.conexion.commit()

	def seleccionar_datos(self, query, parametros=()):
		"""Este método sera llamado para ejecutar la accion de
		consulta de registros, asi como para vertir los 
		mismos en el treeview del modulo maquetacion."""
		self.cursor.execute(query,parametros)
		datos = self.cursor.fetchall()
		return datos

	def crear_tabla(self, nombre):
		"""Este método crea la base de datos en caso de que esta
		todavía no exista. Caso contrario, da aviso por consola."""
		try:
			query = f'''CREATE TABLE {nombre}
				(Código integer primary key AUTOINCREMENT, 
				Nombre text NOT NULL, N_autor text, 
				A_autor text NOT NULL, Precio real NOT NULL
				)'''
			self.get_query(query)
			
		except sqlite3.OperationalError:
			print("La tabla ya existe.")

	def datos_tree(self, parametros=()):
		"""Este metodo toma todos los datos para que sean vertidos
		luego en el treeview del módulo maquetación."""
		query = "SELECT * FROM Librería order by Código DESC"
		return self.seleccionar_datos(query)

	def buscar(self, dato, entrada):
		"""Este metodo toma todos los datos a partir de los 
		parametros asignados por medio del método buscar del 
		módulo logica para luego ser vertidos en el treeview
		del módulo maquetacion."""
		query = f'''SELECT * FROM Librería where {dato} = 
			"{entrada}" order by Código DESC'''
		return self.seleccionar_datos(query)

	def ventana_editar(self, id):
		"""Este método es requerido por el módulo maquetacion para
		obtener los datos del registro seleccionado en el treeview 
		contenido en dicho modulo que a su vez verterá los datos
		obtenidos en la subventana de editar registro"""
		query = f"SELECT * FROM Librería where Código = {id}"
		return self.seleccionar_datos(query)

	def agregar_registro(self, titulo, n_autor, a_autor, precio):
		"""Este metodo contiene el código de alta de registro
		y llama al método get_query con este como argumento"""
		query = "INSERT INTO Librería VALUES(null,?,?,?,?)"
		self.get_query(query,(titulo,n_autor, a_autor, precio))

	def eliminar_registro_db(self, id):
		"""Este metodo contiene el código de baja de registro
		y llama al método get_query con este como argumento"""
		query = f'DELETE FROM Librería where Código == {id}'
		self.get_query(query)

	def actualizar_registro_db(self, id, parametros=()):
		"""Este metodo contiene el código de modificación de registro
		y llama al método get_query con este como argumento"""
		query = f'''UPDATE Librería SET Nombre=?,
			N_autor=?, A_autor=?, Precio=?  where Código == {id}
			'''
		self.get_query(query,parametros)

