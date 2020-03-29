#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 29 del Capítulo 02.
"""


def main():
    """
    Función principal.
    """
    print("0 == 1 == 2 [{}] => 0 == (1 == 2): [{}]".\
          format(0 == 1 == 2, 0 == (1 == 2)))

    print("2 + 3 == 4 + 5 == 7 [{}] => 2 + (3 == 4) + 5 == 7 [{}]".\
          format(2 + 3 == 4 + 5 == 7, 2 + (3 == 4) + 5 == 7))

    print("1 < -1 == 3 > 4 [{}] => (1 < -1) == (3 > 4) [{}]".\
          format(1 < -1 == 3 > 4, (1 < -1) == (3 > 4)))


if __name__ in ("__main__", "__console__"):
    main()
