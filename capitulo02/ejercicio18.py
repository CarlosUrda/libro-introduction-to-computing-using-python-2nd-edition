#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 18 del Capítulo 02.
"""

def main():
    """
    Función principal.
    """
    flowers = ["rose", "bougainvillea", "yucca", "marigold", "daylilly",\
               "lilly of the valley"]
    print(flowers)

    print(f'"potato" in {flowers}:', "potato" in flowers)

    thorny = flowers[:3]
    print("thorny: ", thorny)

    poisonous = flowers[-1:]
    print("poisonous: ", poisonous)

    dangerous = thorny + poisonous
    print("dangerous: ", dangerous)


if __name__ in ("__main__", "__console__"):
    main()
