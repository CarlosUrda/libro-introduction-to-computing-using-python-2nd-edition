#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 31 del Capítulo 02.
"""

import utilidades.util as u


def main():
    """
    Función principal.
    """
    salir = "s"
    print(f"\n(Para salir, introduce {salir} en cualquier momento)")

    try:
        lista = u.obtener_dato("\nIntroduce la lista de números: ",\
                               u.cadena_a_lista_de_numeros, fin=salir)
        print("Lista inicial:", lista)

        lista_aux = u.obtener_dato("Introduce la lista aux: ",\
                                   u.cadena_a_lista_de_numeros, fin=salir)
        print("Lista auxiliar:", lista_aux)

    except EOFError:
        print("Saliendo...")
        return

    lista.extend(lista_aux)
    print(f"lista.extend({lista_aux}) => {lista}")

    lista_copy = lista.copy()
    print(f"lista.copy() => {lista_copy}")

    lista.clear()
    print(f"lista.clear() => {lista}")

    print(f"lista copiada => {lista_copy}")

if __name__ in ("__main__", "__console__"):
    main()
