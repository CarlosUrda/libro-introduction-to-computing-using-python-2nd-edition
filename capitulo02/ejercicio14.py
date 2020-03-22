#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 14 del Capítulo 02
"""

def main():
    """
    Función principal.
    """
    cad = input("Introduce una cadena: ")
    print(f'Primer carácter de "{cad}" es "g": {cad[0] == "g"}')
    print(f'Séptimo carácter de "{cad}" es "g": {cad[6] == "g"}')
    print(f'Primeros dos caracteres de "{cad}" son "ga": {cad[0:2] == "ga"}')
    print(f'Penúltimo carácter de "{cad}" es "x": {cad[-2] == "x"}')
    print(f'El carácter a mitad de "{cad}" es "d": {cad[len(cad)//2] == "d"}')
    print(f'El primer y último carácter "{cad}" son iguales: '\
          f'{cad[0] == cad[-1]}')
    print(f'Los cuatro últimos caracteres de "{cad}" son "tion": '\
          f'{cad[-4:] == "tion"}')


if __name__ in ("__main__", "__console__"):
    main()
