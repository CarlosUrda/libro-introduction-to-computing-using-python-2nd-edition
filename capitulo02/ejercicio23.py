#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 23 del Capítulo 02.
"""

def main():
    """
    Función principal.
    """
    meses_l = ["Ene", "Feb", "Mar", "May"]
    #meses_t = ("Ene", "Feb", "Mar", "May")

    meses_l.insert(meses_l.index("May"), "Abr")
    print(meses_l)

    meses_l.append("Jun")
    print(meses_l)

    meses_l.pop()
    print(meses_l)

    del meses_l[1]
    print(meses_l)

    meses_l.reverse()
    print(meses_l)

    meses_l.sort()
    print(meses_l)



if __name__ in ("__main__", "__console__"):
    main()
