#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 17 del Capítulo 02.
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

    print("17+(-9) < 10: ", 17+(-9) < 10)
    print("len({}) > len(\"{}\")*5: ".\
          format(inventory, fullname), len(inventory) > len(fullname)*5)
    print("not c > 24: ", var_c <= 24)
    print("a < 6.75 < b: ", var_a < 6.75 < var_b)
    print("len(\"{}\") > len(\"{}\") > len(\"{}\"): ".\
          format(last, middle, first), len(last) > len(middle) > len(first))
    print("{0} == [] or len({0}) > 10: ".\
          format(inventory), inventory == [] or len(inventory) > 10)


if __name__ in ("__main__", "__console__"):
    main()
