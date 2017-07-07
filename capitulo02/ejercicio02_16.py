#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 16 del Capítulo 02
"""

def main():
    """
    Función principal.
    """
    var_a = 6
    var_b = 7

    var_c = (var_a+var_b) / 2

    inventory = ["paper", "staples", "pencils"]

    first = "John"
    middle = "Fitzgerald"
    last = "Kennedy"

    fullname = first + " " +  middle + " " + last

    print("a =", var_a)
    print("b =", var_b)
    print("c =", var_c)
    print("inventory =", inventory)
    print("first =", first)
    print("middle =", middle)
    print("last = ", last)
    print("fullname =", fullname)

if __name__ in ("__main__", "__console__"):
    main()
