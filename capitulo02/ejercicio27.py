#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 27 del Capítulo 02.
"""

import math as m
from util import obtener_dato


def main():
    """
    Función principal.
    """
    angulo = obtener_dato("Introduce el ángulo de la escalera con el suelo: ",\
                          float, lambda x: 0 <= x <= 90, ("salir", "fin"))
    if angulo is None:
        print("Saliendo...")
        return

    longitud = obtener_dato("Introduce la longitud de la escalera: ", float,\
                            lambda x: x >= 0, ("salir", "fin"))
    if longitud is None:
        print("Saliendo...")
        return

    radianes = m.pi * angulo / 180
    altura = m.sin(radianes) * longitud
    print("La altura de la escalera es: ", altura)


if __name__ in ("__main__", "__console__"):
    main()
