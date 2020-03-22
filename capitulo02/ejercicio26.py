#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 26 del Capítulo 02.
"""

from ast import literal_eval
from util import es_iterable, obtener_dato


def es_punto(punto):
    """
    Comprobar si un dato es un punto en alguno de los siguientes formatos:
    (x, y); [x, y]; {"x": x, "y", y}
    Las coordenadas x, y pueden ser de tipo int, float o complex.

    Argumentos:
        punto: dato a comprobar si está en formato punto.

    Retorno:
        True si el dato está en formato punto.
        False si el dato no está en formato punto.
    """
    if isinstance(punto, (list, tuple)):
        if len(punto) != 2:
            return False
        coordenadas = punto
    # Se hizo la comprobación para aceptar diccionario pero en la función para
    # comprobar si está dentro del círculo es mucho lío.
    #elif isinstance(punto, dict):
    #    if set(punto.keys()) != {'x', 'y'}:
    #        return False
    #    coordenadas = punto.values()
    else:
        return False

    return all((isinstance(coordenada, (int, float, complex)) \
                for coordenada in coordenadas))


def es_punto_en_circulo(punto, centro, radio):
    """
    Función que comprueba si unas coordenadas están dentro de un círculo.

    Argumentos:
        punto: tupla o lista de dos elementos con las coordenadas (x, y) del
            punto a comprobar.
        centro: tupla o lista de dos elementos con las coordenadas (x, y) del
            centro del círculo.
        radio: número con el valor del radio de la circunferencia.

    Retorno:
        True si el punto está dentro de la circunferencia.
        False si el punto está fuera de la circunferencia.
    """
    distancia2 = (punto[0] - centro[0])**2 + (punto[1] - centro[1])**2
    return distancia2 < radio**2


def main():
    """
    Función principal.
    """
    salir = ("salir", "fin")
    print("PROGRAMA PARA COMPROBAR SI UN PUNTO ESTÁ EN UNA CIRCUNFERENCIA\n")
    print("* Para salir en cualquier momento, escribe alguna:", salir)

    radio = obtener_dato("\nIntroduce el radio: ", float, fin=salir)
    if radio is None:
        return

    centro = obtener_dato("Introduce las coordenadas del centro (x, y): ", \
                          literal_eval, es_punto, fin=salir)
    if centro is None:
        return

    while True:
        punto = obtener_dato("\nIntroduce coordenadas del punto (x, y): ", \
                             literal_eval, es_punto, fin=salir)
        if punto is None:
            break

        esta_dentro = es_punto_en_circulo(punto, centro, radio)
        print("Está dentro" if esta_dentro else "No está dentro")


if __name__ in ("__main__", "__console__"):
    main()
