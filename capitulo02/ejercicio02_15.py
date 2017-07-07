#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 15 del Capítulo 02
"""

def main():
    """
    Función principal.
    """
    var_p1 = "anachronistically"
    var_p2 = "counterintuitive"
    print("len(\"{}\") == 1 + len(\"{}\"): ".\
          format(var_p1, var_p2), len(var_p1) == 1 + len(var_p2))

    var_p1 = "misinterpretation"
    var_p2 = "misrepresentation"
    print("\"{}\" < \"{}\": ".format(var_p1, var_p2), var_p1 < var_p2)

    var_p = "floccinaucinihilipilification"
    print("El cáracter 'e' no aparece en \"{}\": ".format(var_p1), 'e' in var_p)

    var_p1 = "counterrevolution"
    var_p2 = "counter"
    var_p3 = "resolution"
    print("len(\"{}\") == len(\"{}\") + len(\"{}\"): ".\
          format(var_p1, var_p2, var_p3), len(var_p1) == len(var_p2)+len(var_p3))


if __name__ in ("__main__", "__console__"):
    main()
