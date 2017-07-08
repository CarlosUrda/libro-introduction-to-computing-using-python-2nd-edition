#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 26 del Capítulo 02.
"""

from ast import literal_eval

def es_iterable(objeto):
    """
    Comprobar si un objeto es de tipo iterable

    Argumentos:
        objeto: objeto a comprobar si es iterable.

    Retorno:
        True o False si el objeto es o no iterable.
    """
    return hasattr(objeto, "__getitem__") or hasattr(objeto, "__iter__")


def obtener_dato(mensaje, evaluar=None, comprobar=None, fin=None):
    """
    Leer cadenas desde el teclado hasta que una de ellas cumpla alguna de estas
    condiciones:
    - La cadena sea una de las cadenas de finalización.
    - La cadena, una vez evaluada en caso de evaluarse, pase una comprobación.

    Argumentos:
        mensaje: mensaje a ser mostrado antes de introducir el dato por teclado.
        evaluar: función usada para evaluar la cadena introducida y obtener
            el tipo de dato deseado. Debe lanzar una excepción ValueError si
            la cadena a evaluar no tiene el formato correcto. En caso de None
            la cadena leída por teclado no se evalúa.
        comprobar: función que comprueba si el dato introducido (evaluado en
            caso de evaluarse) es correcto. Si es None, no se realiza ninguna
            comprobación del dato.
            Debe devolver True si el dato es correcto o False en caso contrario.
        fin: cadena o lista de cadenas de finalización que interrumpe la lectura
            por teclado. Si es None no se realiza ninguna comprobación de
            finalización de la cadena introducida por teclado.

    Retorno:
        Los posibles valores devueltos son:
        - None si la cadena leída es una cadena de finalización.
        - Dato introducido por teclado ya evaluado y pasada la comprobación.
    """
    while True:
        dato = input(mensaje).strip()
        if fin is not None and \
           (es_iterable(fin) and str.lower(dato) in map(str.lower, fin) or \
            not es_iterable(fin) and str.lower(dato) == str.lower(fin)):
            return None

        if evaluar is not None:
            try:
                dato = evaluar(dato)
            except ValueError:
                print("ERROR: fallo al evaluar la cadena introducida.")
                continue

        if comprobar is None or comprobar(dato):
            return dato

        print("ERROR: el dato está en formato incorrecto.")


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
