#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 12 del Capítulo 02
"""

def main():
    """
    Función principal.
    """
    cad1 = '-'
    cad2 = '+'

    print(cad1+cad2)
    print(cad1+cad2+cad1)
    print(cad2+cad1*2)
    print((cad2+cad1*2)*2)
    print(cad2+(cad1*2+cad2)*10)
    print((cad2+cad1+cad2*3+cad1*2)*5)


if __name__ in ("__main__", "__console__"):
    main()
