#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 27 del Capítulo 02.
"""

import math 
from utilidades.util import obtener_dato


def main():
    """
    Función principal.
    """
    print("\n*** PROGRAMA PARA CALCULAR LA ALTURA DE UNA ESCALERA ***\n")
    salir = "s"
    print(f"\n(Para salir, introduce {salir} en cualquier momento)")

    while True:
        try:
            angulo = obtener_dato("\nIntroduce ángulo de escalera y suelo: ",\
                                  float, lambda x: 0 <= x <= 90, salir,\
                                  "Debes introducir un número.",\
                                  "El ángulo debe ser entre 0 y 90 grados.")

            longitud = obtener_dato("\nIntroduce longitud de la escalera: ",\
                                    float, lambda x: x >= 0, salir,\
                                    "Debes introducir un número.",\
                                    "La longitud debe ser >= 0.")
        except EOFError:
            print("\nSaliendo...")
            return

        radianes = math.pi * angulo / 180
        altura = math.sin(radianes) * longitud
        print("La altura de la escalera es: ", altura)


if __name__ in ("__main__", "__console__"):
    main()
