#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 28 del Capítulo 02
"""

import utilidades.util as u


def main():
    """
    Función principal
    """

    salir = "s"
    print(f"\n(Para salir, introduce {salir} en cualquier momento)")

    try:
        lista = u.obtener_dato("\nIntroduce la lista de números: ",\
                               u.cadena_a_lista_de_numeros, bool, salir,\
                               "Debes introducir números en formato corecto.",\
                               "Debes introducir algún número.")
    except EOFError as e:
        print("\nSaliendo...")
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
