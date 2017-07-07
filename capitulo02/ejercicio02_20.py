#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 20 del Capítulo 02.
"""

def main():
    """
    Función principal.
    """
    while True:
        cadena = input("Introduce una cadena de 3 letras: ").strip()
        if len(cadena) == 3:
            break

    print("La cadena introducida es:", cadena)

    print("La cadena al revés es:", cadena[-1::-1])


if __name__ in ("__main__", "__console__"):
    main()
