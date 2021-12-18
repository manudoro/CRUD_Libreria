"""Este modulo se ocupa de la logica de la aplicación, conectando
al modulo que contiene la maquetación de la GUI con el que realiza 
la interacción con la base de datos"""
from tkinter import messagebox

import validacion
import conexioncondb
class Logica:
	"""En esta clase se engloban los métodos encargados de la logica
	de la aplicación"""	
	def __init__(self):
		"""Dentro de este método se declara una instancia de la clase
		Crud para interactuar con la base de datos"""
		self.db = conexioncondb.Crud()

	def mostrar_registros(self, tree, aviso):
		"""Este método vierte los registros vigentes en la base 
		dentro del Treeview de la interfaz"""
		registros_viejos = tree.get_children()
		for registro in registros_viejos:
			tree.delete(registro)
		datos = self.db.datos_tree()
		for dato in datos:
			tree.insert('','0', text=dato[0], values=(
				dato[1],dato[3]+', '+str(dato[2]),dato[4]))
		aviso['text'] = 'Bienvenido a la aplicación Librería'

	def buscar(self, dato, entrada, tree, aviso):
		"""Este método vierte los registros solicitados por el 
		usuario en la barra de busqueda de la aplicación dentro 
		del Treeview de la misma."""
		busqueda = self.db.buscar(dato,entrada)
		registros_viejos = tree.get_children()
		for registro in registros_viejos:
			tree.delete(registro)
		for dato in busqueda:
				tree.insert('','0', text=dato[0], values=(
				dato[1],dato[3]+', '+str(dato[2]),dato[4]))	
		if len(busqueda) == 0:
			aviso['text'] = f"No se hallaron resultados"
		else:
			aviso['text'] = f"Se hallaron {len(busqueda)} resultados"

	def agregar_registro(
			self, titulo, n_autor,a_autor, 
			precio, tree, ventana, aviso):
		"""Este método define una instancia de la clase Validacion
		contenida en el módulo validacion y coteja que los datos
		ingresados en la ventana de añadir registro sean validos.
		En caso afirmativo, utiliza una función del modulo 
		conexioncondb para realizar el alta de registro."""
		validar = validacion.Validacion()
		if validar.validar_titulo(titulo) == False:
			messagebox.showwarning(
				"Atención", "El Título ingresado no es válido."
				)
		elif validar.validar_nautor(n_autor) == False:
			messagebox.showwarning(
				"Atención", "El Nombre ingresado no es válido."
				)
		elif validar.validar_aautor(a_autor) == False:
			messagebox.showwarning(
				"Atención", "El Apellido ingresado no es válido."
				)
		elif validar.validar_precio(precio) == False:
			messagebox.showwarning(
				"Atención", "El Precio ingresado no es válido."
				)
		else:
			self.db.agregar_registro(titulo, n_autor, a_autor, precio)
			self.mostrar_registros(tree,aviso)
			ventana.destroy()
			aviso['text'] = "Registro añadido"

	def eliminar_registro(self, tree, aviso):
		"""Este método llama al metodo eliminar_registro_db del módulo
		conxexioncondb para dar de baja un registro seleccionado"""
		try:
			reg = tree.selection()[0]
			db_reg = tree.item(tree.selection())['text']
			response = messagebox.askquestion(
				"Atención", "¿Seguro que desea eliminar el registro" 
				+ str(db_reg) + '?')
			if response == 'yes':
				self.db.eliminar_registro_db(db_reg)
				tree.delete(reg)
				self.mostrar_registros(tree,aviso)
				aviso['text'] = f"Registro {db_reg} eliminado"

		except IndexError:
			aviso['text'] = "Por favor seleccione un item"
	
	def editar_registro(
			self, titulo, n_autor, a_autor, 
			precio, tree, ventana, aviso):
		"""Este método define una instancia de la clase Validacion
		contenida en el módulo validacion y coteja que los datos
		ingresados en la ventana de editar registro sean validos.
		En caso afirmativo, utiliza una función del modulo 
		conexioncondb para realizar la modificación de registro."""
		db_reg = tree.item(tree.selection())['text']
		validar = validacion.Validacion()
		if validar.validar_titulo(titulo) == False:
			messagebox.showwarning(
				"Atención", "El Título ingresado no es válido."
				)
		elif validar.validar_nautor(n_autor) == False:
			messagebox.showwarning(
				"Atención", "El Nombre ingresado no es válido."
				)
		elif validar.validar_aautor(a_autor) == False:
			messagebox.showwarning(
				"Atención", "El Apellido ingresado no es válido."
				)
		elif validar.validar_precio(precio) == False:
			messagebox.showwarning(
				"Atención", "El Precio ingresado no es válido."
				)
		else:
			self.db.actualizar_registro_db(
				db_reg, (titulo, n_autor, a_autor, precio))
			self.mostrar_registros(tree,aviso)
			ventana.destroy()
			aviso['text'] = "Registro actualizado"
