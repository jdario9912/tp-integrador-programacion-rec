import lista
import arbol
import utils


inicio = utils.timer()
print("Generando arbol...")
arbol.generar_arbol()
fin = utils.timer()
utils.mostrar_tiempo("Tiempo de generacion del arbol", inicio, fin)

busqueda = "Bed modern sport"
print(f"\n\nLibro a buscar: {busqueda}")

print("Buscando libro en lista...")
inicio = utils.timer()
lista.buscar_en_lista(busqueda)
fin = utils.timer()
utils.mostrar_tiempo("Tiempo de busqueda en lista", inicio, fin)

print("\nBuscando libro en el arbol...")
inicio = utils.timer()
arbol.buscar_en_arbol(busqueda)
fin = utils.timer()
utils.mostrar_tiempo("Tiempo de busqueda en arbol", inicio, fin)

busqueda = "Young establish unit"
print(f"\n\nLibro a buscar: {busqueda}")

print("Buscando libro en lista...")
inicio = utils.timer()
lista.buscar_en_lista(busqueda)
fin = utils.timer()
utils.mostrar_tiempo("Tiempo de busqueda en lista", inicio, fin)

print("\nBuscando libro en el arbol...")
inicio = utils.timer()
arbol.buscar_en_arbol(busqueda)
fin = utils.timer()
utils.mostrar_tiempo("Tiempo de busqueda en arbol", inicio, fin)
