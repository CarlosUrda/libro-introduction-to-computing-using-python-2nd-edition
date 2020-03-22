#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 11 del Capítulo 2
"""

def main():
    """
    Función principal.
    """
    print("Suma -7=>-1:", sum(range(-7, 0)))


    alumnos_edad = {9: 17, 10: 24, 11: 21, 12: 27}

    total_alumnos = total_edades = 0
    for edad, alumnos in alumnos_edad.items():
        total_alumnos += alumnos
        total_edades += alumnos * edad

    print("Media de edad:", total_edades / total_alumnos)


    print("2^-20:", 2**-20)

    print("Veces 61 en 4356:", 4356 // 61)

    print("Resto 4356/61:", 4356 % 61)


if __name__ in ("__main__", "__console__"):
    main()
