#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 22 del Capítulo 02.
"""

def main():
    """
    Función principal.
    """
    numeros = None
    while numeros is None:
        datos = input("Introduce la lista de números: ").strip().split()
        if datos == []:
            continue
        try:
            numeros = [int(numero) for numero in datos]
        except ValueError:
            print("ERROR: Introduce números enteros separados por espacios.")

    numeros.sort()
    print("Lista de números introducida:", numeros)
    print("Rango:", max(numeros) - min(numeros))


if __name__ in ("__main__", "__console__"):
    main()
