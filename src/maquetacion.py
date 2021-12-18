"""Este módulo abarca el código referido a la maquetación de
la aplicación, realizada a partir del paquete tkinter"""

# Importo el OperationalError para capturar el posible error
# de la línea 145.
from sqlite3 import OperationalError
# Entiendo que es una forma de importación ineficiente pero
# lo encuentro más cómodo que especificar uno por uno todos 
# los widgets del paquete tkinter a utilizar.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import logica
import conexioncondb


class Maquetacion:
	"""En está clase se engloban todos los atributos y metodos 
	referidos al diseño de la aplicación"""
	def __init__(self, window):
		"""Este metodo define el mapeo de la ventana al iniciarse
		una instancia la misma"""
		# Configuro la ventana principal
		self.window = window
		self.window.title("Librería")
		self.window.resizable(False, False)
		self.window.config(bg='#c8f7c6')
		self.window.bind('<Return>', 
			lambda event:self.logica.buscar(
				self.busqueda.get(), self.entrada_busqueda.get(), 
				self.tree, self.aviso)
		)
		# Creo la instancia db de la clase Crud para interactuar 
		# con el módulo conexioncondb.
		self.db = conexioncondb.Crud()
		self.db.crear_tabla('Librería')
		self.logica = logica.Logica()
		# Creo una tabla donde se mostrará la información
		self.tree_frame = Frame(self.window)
		self.tree_frame.config(bg='#c8f7c6')
		self.tree_frame.grid(row=0, column=0, rowspan=10, 
			columnspan=12, padx=5
			)
		self.tree = ttk.Treeview(self.tree_frame)
		self.tree['columns'] = ('col1', 'col2', 'col3')
		self.tree.column("#0", width=50, minwidth=30, anchor=W, stretch=NO)
		self.tree.column("col1", width=250, minwidth=80, stretch=NO)
		self.tree.column("col2", width=150, minwidth=80, stretch=NO)
		self.tree.column("col3", width=50, minwidth=50)
		self.tree.heading('#0', text='Código', anchor=CENTER)
		self.tree.heading('col1', text='Título', anchor=CENTER)
		self.tree.heading('col2', text='Autor', anchor=CENTER)
		self.tree.heading('col3', text='Precio', anchor=CENTER)
		self.tree_scroll = Scrollbar(self.tree_frame)
		self.tree_scroll.configure(command=self.tree.yview)
		self.tree_scroll.pack(side=RIGHT, fill=Y)
		self.tree.configure(yscrollcommand = self.tree_scroll.set)
		self.tree.pack()
		self.aviso_frame = Frame(self.window, bg='#c8f7c6')
		self.aviso_frame.grid(row=11, column=0, columnspan=12)
		self.aviso = Label(self.aviso_frame)
		self.aviso.config(bg='#c8f7c6',font=8)
		self.aviso['text'] = "Bienvenido a la aplicación Librería"
		self.aviso.pack()
		self.logica.mostrar_registros(self.tree, self.aviso)
		# Creo botones para la ventana principal0
		self.boton_anadir = Button(self.window, text='Añadir registro', 
			command=self.ventana_anadir, bg='#ddf7dc')
		self.boton_anadir.grid(row=1, column=13,pady=5, padx=5, ipadx=6)
		self.boton_editar = Button(self.window, text='Editar registro',
			command=self.ventana_editar_registro, bg='#ddf7dc')
		self.boton_editar.grid(row=4, column=13,pady=5, padx=5, ipadx=8)
		self.boton_eliminar = Button(
			self.window, text='Eliminar registro', 
			bg='#ddf7dc', command=lambda:self.logica.eliminar_registro(
				self.tree, self.aviso)) 
		self.boton_eliminar.grid(row=7, column=13,pady=5, padx=5)
		self.boton_restaurar = Button(
			self.window,text='Restaurar', bg='#ddf7dc',
			command=lambda:self.logica.mostrar_registros(self.tree,self.aviso))
		self.boton_restaurar.grid(row=12, column=13,pady=5, ipadx=20)
		# Configuro la barra de búsqueda
		self.busqueda_label = Label(self.window, text='Buscar por:')
		self.busqueda_label.grid(row=12, column=0, sticky=W)
		self.busqueda_label.config(bg='#c8f7c6')
		self.opciones_busqueda = [
			('Código','Código'),('Título','Nombre'),('Apellido','A_autor')
			]
		self.busqueda = StringVar()
		self.busqueda.set('A_autor')
		columna = 1
		for texto, valor in self.opciones_busqueda:
			Radiobutton(self.window, text=texto, variable=self.busqueda,
				value=valor, bg='#c8f7c6').grid(row=12,column=columna, sticky=W
				)
			columna += 1
		self.entrada_busqueda = Entry(self.window, bg='#ecffe8')
		self.entrada_busqueda.grid(row=12, column=4)
		self.entrada_busqueda.focus()
		self.imagen = PhotoImage(file="img/lupa2.png") 
		self.boton_busqueda = Button(self.window,
			command=lambda:self.logica.buscar(self.busqueda.get(),
				self.entrada_busqueda.get(),self.tree, self.aviso) 
		)
		self.boton_busqueda.config(image=self.imagen, 
			width=17, height=17, bg='#ddf7dc')
		self.boton_busqueda.grid(row=12, column=5)

	
	def ventana_anadir(self):
		"""Este metodo define una ventana secundaria que provee
		la interfaz para añadir registros en la base"""
		self.subana = Toplevel()
		self.subana.title("Añadir registro...")
		self.subana.resizable(False, False)
		self.subana.bind(
			'<Return>', lambda event: self.logica.agregar_registro(
				titulo.get(), n_autor.get(), a_autor.get(), precio.get(),
				self.tree, self.subana, self.aviso))
		self.subana.config(bg='#c8f7c6')
		Label(self.subana, text='Título: ', bg='#c8f7c6').grid(
			row=0, column=0, pady=5, sticky=W)
		titulo = Entry(self.subana, width=40, bg='#ecffe8')
		titulo.grid(row=0, column=1, pady=5, padx=10, sticky=W)
		Label(self.subana, text='Nombre de autor: ', 
			bg='#c8f7c6').grid(row=1, column=0, pady=5)
		n_autor = Entry(self.subana, width=40, bg='#ecffe8')
		n_autor.grid(row=1, column=1, pady=5, padx=10)
		Label(self.subana, text='Apellido de autor: ', 
			bg='#c8f7c6').grid(row=2, column=0, pady=5, sticky=W)
		a_autor = Entry(self.subana, width=40, bg='#ecffe8')
		a_autor.grid(row=2, column=1, pady=5, padx=10)
		Label(self.subana, text='Precio: ', bg='#c8f7c6').grid(
			row=3, column=0, pady=5, sticky=W
			)
		precio = Entry(self.subana, width=40, bg='#ecffe8')
		precio.grid(row=3, column=1, pady=5, padx=10)
		submit = Button(self.subana, text='Añadir', bg='#ddf7dc',
			command=lambda: self.logica.agregar_registro(titulo.get(),
			n_autor.get(), a_autor.get(), precio.get(),
			self.tree, self.subana, self.aviso))
		submit.grid(row=4, column=0, columnspan=2, ipadx=20, pady=5)
	
	def ventana_editar_registro(self):
		"""Este metodo define una ventana secundaria que provee
		la interfaz para realizar modificaciones en los registros
		ya cargados a la base"""
		try:
			registros = self.tree.item(self.tree.selection())['text']
			lista = self.db.ventana_editar(registros)
		except OperationalError:
			self.aviso['text'] = "Por favor seleccione un item"
			return
		self.subedi = Toplevel()
		self.subedi.title("Editar registro...")
		self.subedi.resizable(False, False)
		self.subedi.config(bg='#c8f7c6')
		Label(self.subedi, text='Título: ', 
			bg='#c8f7c6').grid(row=0, column=0, pady=5, sticky=W)
		self.subedi.bind(
			'<Return>', 
			lambda event: self.logica.editar_registro(
				titulo.get(), n_autor.get(), a_autor.get(), precio.get(),
				self.tree, self.subedi, self.aviso)
			)		
		titulo = Entry(self.subedi, width=40, bg='#ecffe8')
		titulo.grid(row=0, column=1, pady=5, padx=10)
		Label(self.subedi, text=' Nombre de autor: ',
			bg='#c8f7c6').grid(row=1, column=0, pady=5, sticky=W)
		n_autor = Entry(self.subedi, width=40, bg='#ecffe8')
		n_autor.grid(row=1, column=1, pady=5, padx=10)
		Label(self.subedi, text=' Apellido de autor: ',
			bg='#c8f7c6').grid(row=2, column=0, pady=5, sticky=W)
		a_autor = Entry(self.subedi, width=40, bg='#ecffe8')
		a_autor.grid(row=2, column=1, pady=5, padx=10)
		Label(self.subedi, text='Precio:   $', bg='#c8f7c6').grid(
			row=3, column=0, pady=5, sticky=W
			)
		precio = Entry(self.subedi, width=40, bg='#ecffe8')
		precio.grid(row=3, column=1, pady=5, padx=10)

		registros = self.tree.item(self.tree.selection())['text']
		lista = self.db.ventana_editar(registros)
		for datos in lista:
			titulo.insert(0, datos[1])
			n_autor.insert(0, datos[2])
			a_autor.insert(0, datos[3])
			precio.insert(0, datos[4])
		edit = Button(self.subedi, text='Confirmar', bg='#ddf7dc',
		 	command=lambda: self.logica.editar_registro(titulo.get(),
		 		n_autor.get(), a_autor.get(), precio.get(),
		 		self.tree, self.subedi, self.aviso))
		edit.grid(row=4, column=0, columnspan=2, ipadx=10, pady=5)
