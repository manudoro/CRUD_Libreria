"""Este script realiza la ejecución de la aplicación, creando una
instancia de la clase Maquetacion en caso de que sea ejecutado como
__main__."""

from tkinter import Tk
from maquetacion import Maquetacion

if __name__ == '__main__': 
	root = Tk()
	programa = Maquetacion(root)
	root.mainloop()
