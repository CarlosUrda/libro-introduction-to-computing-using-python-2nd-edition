#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 24 del Capítulo 02
"""

import random
from collections import Counter
from collections import defaultdict


def obtener_dato(mensaje, tipo):
    """
    Obtener un dato del teclado y convertirlo a un tipo concreto.

    Argumentos:
        mensaje: mensaje a ser mostrado antes de introducir el dato por teclado.
        tipo: tipo a ser convertida el dato de la entrada de teclado.
    """
    while True:
        dato = input(mensaje).strip()
        try:
            dato = tipo(dato)
        except ValueError:
            print("ERROR: tienes que introducir un", tipo.__name__)
        else:
            break

    return dato


def main():
    """
    Función principal
    """
    notas_posibles = ['A', 'B', 'C', 'D', 'E', 'F']

    num_notas = obtener_dato("Introduce el número de notas: ", int)

    num_notas_posibles = len(notas_posibles)
    notas = [notas_posibles[random.randrange(0, num_notas_posibles)]\
                for _ in range(num_notas)]
    print("Notas:", notas)

    frec_notas1 = defaultdict(int)
    for nota in notas:
        frec_notas1[nota] += 1
    print("Frecuencia notas:", frec_notas1)

    frec_notas2 = Counter(notas)
    print(frec_notas2)

    print(list(zip(*sorted(frec_notas2.items()))))


if __name__ in ("__main__", "__console__"):
    main()
