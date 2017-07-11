#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 19 del Capítulo 02
"""

def main():
    """
    Función principal.
    """
    answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
    print("answers:", answers)

    num_yes = answers.count('Y')
    print("Número de 'Y'es:", num_yes)

    num_nes = answers.count('N')
    print("Número de 'N'es:", num_nes)

    percentYes = num_yes * 100 / len(answers)
    print("Porcentaje de 'Y':", percentYes)

    answers.sort()
    print("answers ordenada:", answers)

    f = answers.index('Y')
    print("Índice de primera ocurrencia de 'Y':", f)


if __name__ in ("__main__", "__console__"):
    main()
