#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 13 del Capítulo 03
"""

def main():
    """
    Función principal.
    """
    cad = "abcdefghijklmnopqrstuvwxyz"
    print(cad[0])
    print(cad[cad.find('c')])
    print(cad[-1])
    print(cad[-2])
    print(cad[cad.index('q')])


if __name__ in ("__main__", "__console__"):
    main()
