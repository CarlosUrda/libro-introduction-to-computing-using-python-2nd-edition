#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 31 del Capítulo 02.
"""

from ast import literal_eval
import util


def main():
    """
    Función principal.
    """
    lista = util.obtener_dato("Introduce la lista: ", literal_eval,\
                              lambda x: isinstance(x, list), ("fin", "salir"))
    if lista is None:
        print("Saliendo...")
        return

    print("Lista inicial:", lista)

    lista_aux = util.obtener_dato("Introduce la lista aux: ", literal_eval,\
                                lambda x: isinstance(x, list), ("fin", "salir"))
    if lista_aux is None:
        print("Saliendo...")
        return

    lista.extend(lista_aux)
    print("lista.extend({}) => {}".format(lista_aux, lista))

    lista_copy = lista.copy()
    print("lista.copy() => {}".format(lista_copy))

    lista.clear()
    print("lista.clear() => {}".format(lista))

    print("lista copiada => {}".format(lista_copy))

if __name__ in ("__main__", "__console__"):
    main()
