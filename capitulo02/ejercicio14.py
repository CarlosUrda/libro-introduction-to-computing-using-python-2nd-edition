#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 14 del Capítulo 02
"""

def main():
    """
    Función principal.
    """
    cad = input("Introduce una cadena: ")
    print("Primer carácter de \"{}\" es 'g': {}".format(cad, cad[0] == 'g'))
    print("Séptimo carácter de \"{}\" es 'g': {}".format(cad, cad[6] == 'g'))
    print("Primeros dos caracteres de \"{}\" son 'ga': {}".\
          format(cad, cad[0:2] == "ga"))
    print("Penúltimo carácter de \"{}\" es 'x': {}".format(cad, cad[-2] == 'x'))
    print("El carácter a mitad de \"{}\" es 'd': {}".\
          format(cad, cad[len(cad)//2] == 'd'))
    print("El primer y último carácter \"{}\" son iguales: {}".\
          format(cad, cad[0] == cad[-1]))
    print("Los cuatro últimos caracteres de \"{}\" son \"tion\": {}".\
          format(cad, cad[-4:] == "tion"))


if __name__ in ("__main__", "__console__"):
    main()
