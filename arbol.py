from libros import libros
from clases.libro import Libro
from clases.arbol_binario import ArbolBinarioBusqueda

arbol = ArbolBinarioBusqueda()


def generar_arbol():
    for libro in libros:
        libro_a_guardar = Libro(libro["titulo"], libro["autor"], libro["isbn"])
        arbol.insertar(libro_a_guardar)


def buscar_en_arbol(busqueda):
    arbol.buscar(busqueda)
