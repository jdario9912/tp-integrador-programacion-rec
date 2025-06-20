from libros import libros


def buscar_en_lista(busqueda):
    for libro in libros:
        if libro["titulo"] == busqueda:
            break
