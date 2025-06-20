import time


def timer():
    return time.time()


def mostrar_tiempo(mensaje, inicio, fin):
    print(f"{mensaje}: {fin - inicio}ms")
