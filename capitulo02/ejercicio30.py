#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 30 del Capítulo 02.
"""

import utilidades.util as u


def main():
    """
    Función principal.
    """
    cadena = u.obtener_dato("Introduce la cadena: ")
    print("Cadena introducida:", cadena)

    lista = list(cadena)
    print("Lista convertida:", lista)


if __name__ in ("__main__", "__console__"):
    main()
