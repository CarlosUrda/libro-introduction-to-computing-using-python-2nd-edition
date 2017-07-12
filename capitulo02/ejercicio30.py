#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 30 del Capítulo 02.
"""

import util


def main():
    """
    Función principal.
    """
    cadena = util.obtener_dato("Introduce la cadena: ")
    print("Cadena introducida:", cadena)

    lista = list(cadena)
    print("Lista convertida:", lista)


if __name__ in ("__main__", "__console__"):
    main()
