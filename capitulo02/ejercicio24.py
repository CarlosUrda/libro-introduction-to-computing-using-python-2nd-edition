#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 24 del Capítulo 02
"""

import random
from collections import Counter
from collections import defaultdict
from utilidades.util import obtener_dato as leer
from utilidades.util import cadena_a_lista
from utilidades.util import es_subiterable


NOTAS_EXISTENTES = ['A', 'B', 'C', 'D', 'E', 'F']



def main():
    """
    Función principal
    """
    while True:
        try:
            notas = leer("Introduce notas [A-F] posibles separadas por comas:",\
                         lambda x: cadena_a_lista(x, ',', 0b01101111),\
                         lambda x: es_subiterable(x, NOTAS_EXISTENTES), "Fin",\
                         "Introduce una cadena de notas.",\
                         "Introduce notas, separadas por comas, entre A-F.")

            print("Las notas introducidas son:", notas)

            num_notas = leer("Introduce el número de notas a generar: ", int,\
                             lambda x: x > 0, None, "Número debe ser entero",\
                             "El número debe ser positivo")
        except EOFError:
            print("\n\nSaliendo...")
            break

        notas_generadas = [random.choice(notas) for _ in range(num_notas)]
        print("Notas:", notas_generadas)

        frec_notas1 = defaultdict(int)
        for nota in notas_generadas:
            frec_notas1[nota] += 1
        print("Frecuencia notas:", frec_notas1)

        frec_notas2 = Counter(notas_generadas)
        print(frec_notas2)

        print(list(zip(*sorted(frec_notas2.items())))[1])


if __name__ in ("__main__", "__console__"):
    main()
