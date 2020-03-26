#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 26 del Capítulo 02.
"""

import re
from ast import literal_eval
from functools import reduce
from utilidades.util import obtener_dato, cadena_a_lista


def cadena_a_punto(cadena):
    """
    Convertir una cadena a una lista de coordenadas de un punto. 

    Argumentos:
        cadena: cadena de caracteres con los valores separados de las
            coordenadas de un punto. Los valores pueden ser cualquier tipo de
            número. Ignora cualquier carácter que no sea número, ., +, - o j.

    Retorno:
        Lista con los valores de las coordenadas convertidas a números. 

    Excepciones:
        TypeError: argumento no tiene tipo de dato correcto => cadena = str 
        ValueError: los números de las coordenadas en la cadena tienen un
            formato incorrecto.
    """
    if not isinstance(cadena, str):
        raise TypeError(f"Argumento cadena {type(cadena).__name__} no es str.")

    punto = list(filter(bool, re.findall(r"[\d\.\+\-j]+", cadena)))

    if not punto:
        raise ValueError("Debe existir algún número como coordenada.")

    try:
        punto = list(map(literal_eval, punto))
    except (SyntaxError, ValueError) as e:
        raise ValueError("Formato incorrecto de números")

    return punto
  


def es_punto_en_circulo(punto, centro, radio):
    """
    Comprueba si las coordenadas de un punto están dentro de una circunferencia
    o de una esfera. No hay límite en el número de coordenadas, pero deben ser
    el mismo número para el punto y el centro.

    Argumentos:
        punto: secuencia con las coordenadas del punto a comprobar.
        centro: secuencia con las coordenadas del centro de la circunferencia
            o esfera.
        radio: número con el valor del radio de la circunferencia o esfera.

    Retorno:
        True/False si el punto está dentro/fuera de la circunferencia o esfera.

    Excepciones:
        TypeError: argumentos con formato incorrecto
        ValueError: argumentos punto y centro con distinto número de coord.
    """
    try:
        if len(punto) != len(centro):
            raise ValueError("Argumentos con distino número de coordenadas.")
       
        distancia2 = sum(map(lambda x: (x[0]-x[1])**2, zip(punto, centro)))
        return distancia2 < radio**2

    except TypeError as e:
        raise TypeError("Argumentos con formato incorrecto", e)



def main():
    """
    Función principal.
    """
    print("\n*** PROGRAMA PARA COMPROBAR SI UN PUNTO ESTÁ EN UN CÍRCULO ***\n")
    salir = "s"
    print(f"\n(Para salir, introduce {salir} en cualquier momento)")

    try:
        radio = obtener_dato("\nIntroduce el radio: ", float, fin=salir,\
                             mens_err_conv="Debes introducir un número")
        print("Radio:", radio)
        centro = obtener_dato("Introduce coordenadas del centro: ",\
                              cadena_a_punto, fin=salir,\
                              mens_err_conv="Debes introducir un número "\
                                  "correcto por coordenada:")
        print("Centro:", centro)

        while True:
            punto = obtener_dato("\nIntroduce coordenadas del punto: ",\
                                 cadena_a_punto, fin=salir,\
                                 mens_err_conv="Debes introducir un número "\
                                     "correcto por coordenada:")
            print("Punto:", punto)

            try:
                esta_dentro = es_punto_en_circulo(punto, centro, radio)
            except (ValueError, TypeError) as e:
                print("No se puede comprobar si punto está en círculo:", e)
            else:
                print("\nSí" if esta_dentro else "No", "está dentro\n")

    except EOFError as e:
        print("\nSaliendo...")
        return


if __name__ in ("__main__", "__console__"):
    main()
