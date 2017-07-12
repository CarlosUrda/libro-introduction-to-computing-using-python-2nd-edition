#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 28 del Capítulo 02
"""

from ast import literal_eval
import util


def main():
    """
    Función principal
    """
    lista = util.obtener_dato("Introduce la lista de números: ", literal_eval,\
                              util.es_secuencia_numeros, ("salir", "fin"))
    if lista is None:
        print("Saliendo...")
        return

    indice_medio = len(lista) // 2
    print("Índice medio:", indice_medio)

    elemento_medio = lista[indice_medio]
    print("Elemento medio:", elemento_medio)

    lista_ordenada = sorted(lista, reverse=True)
    print("Lista ordenada desc:", lista_ordenada)

    lista_final = lista_ordenada[1:] + lista_ordenada[0:1]
    print("Primer elemento al final", lista_final)


if __name__ in ("__main__", "__console__"):
    main()
