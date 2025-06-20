from .nodo import Nodo


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, libro):
        if self.raiz is None:
            self.raiz = Nodo(libro)
        else:
            self._insertar(libro, self.raiz)

    def _insertar(self, libro, nodo):
        if libro.titulo < nodo.libro.titulo:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(libro)
            else:
                self._insertar(libro, nodo.izquierdo)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(libro)
            else:
                self._insertar(libro, nodo.derecho)

    def buscar(self, titulo):
        return self._buscar(titulo, self.raiz)

    def _buscar(self, titulo, nodo):
        if nodo is None:
            return None
        if titulo == nodo.libro.titulo:
            return nodo.libro
        elif titulo < nodo.libro.titulo:
            return self._buscar(titulo, nodo.izquierdo)
        else:
            return self._buscar(titulo, nodo.derecho)
