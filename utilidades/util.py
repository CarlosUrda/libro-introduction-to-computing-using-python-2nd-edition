#/usr/bin/env python3
#!coding=utf-8

"""
Módulo con utilidades para los ejercicios del libro.
"""

import collections as collec
import numbers as num


def es_secuencia_numeros(objeto):
    """
    Comprobar si un objeto es una secuencia de números.

    Argumentos:
        objeto: objeto a comprobar si es secuencia de números.

    Retorno:
        True o False si el objeto es o no una secuencia de números.
    """
    return isinstance(objeto, collec.Sequence) and \
           all((isinstance(e, num.Number) for e in objeto))


def es_iterable(objeto):
    """
    Comprobar si un objeto es de tipo iterable

    Argumentos:
        objeto: objeto a comprobar si es iterable.

    Retorno:
        True o False si el objeto es o no iterable.
    """
    return hasattr(objeto, "__getitem__") or hasattr(objeto, "__iter__")


def obtener_dato(mensaje, evaluar=None, comprobar=None, mens_err_eva=None,\
                 mens_err_com=None):
    """
    Lee una cadena desde el teclado hasta que cumpla las siguientes condiciones:
    - La llamada a la función comprobar() pasando la cadena leída debe devolver
    True. La cadena leída intenta evaluarse antes de llamar a comprobar(); si se
    evalúa correctamente se pasa la cadena evaluada, y si no se pasa la cadena
    leída originalmente.
    - En caso de no existir comprobar(), la llamada a la función evaluar()
    pasando la cadena leída no debe generar ninguna excepción ValueError o
    SyntaxError.

    Mientras no se cumplan las condiciones anteriores se volverá a pedir la
    lectura de una cadena desde teclado hasta que se cumplan.

    Argumentos:
        mensaje: mensaje a ser mostrado antes de introducir el dato por teclado.
        evaluar: función usada para evaluar la cadena introducida y obtener
            el tipo de dato deseado. Debe lanzar una excepción ValueError o
            SyntaxError si la cadena a evaluar no tiene el formato correcto. En
            caso de None la cadena leída por teclado no se evalúa.
        comprobar: función que comprueba si el dato introducido (evaluado en
            caso de evaluarse correctamente) cumple las condiciones deseadas.
            Si es None, no se realiza ninguna comprobación del dato.
            Devuelve True o False si el dato cumple o no las condiciones.
        mens_err_eva: mensaje de error a mostrar en caso de que no se pueda
            evaluar el dato (ValueError o SyntaxError) y no haya comprobación
            (comprobar is None). El mensaje se imprime junto con el mensaje
            interno de la excepción generada por evaluar(). Si es None, no se
            imprime ningún mensaje (ni el interno de la excepción).
        mens_err_com: mensaje de error a mostrar en caso de no cumplirse las
            condiciones de la función comprobar(). Si es None, no se imprime
            ningún mensaje.

    Retorno:
        Dato introducido por teclado ya evaluado y pasada la comprobación.

    Excepciones:
        Lanza TypeError si alguno de los parámetros evaluar o comprobar no es
        una función callable.
        Si la función evaluar() genera alguna excepción distinta a ValueError
        o SyntaxError, se termina lanzando dicha excepción.
        Si la función comprobar() genera alguna excepción, se termina lanzando
        dicha excepción.

    Notas
        Los parámetros evaluar y comprobar actuarán como funciones sobre los
        datos introducidos por teclado. Tener cuidado de no pasar funciones
        como eval.
    """
    while True:
        dato = input(mensaje).strip()

        try:
            if evaluar is not None:
                dato = evaluar(dato)
        except TypeError as error:
            raise TypeError("ERROR [al llamar a evaluar()]:", error)
        except (ValueError, SyntaxError) as error:
            if comprobar is None and mens_err_eva is not None:
                print("ERROR:", mens_err_eva, '['+error+']')
        else:
            if comprobar is None:
                return dato

        try:
            if comprobar(dato):
                return dato
            if mens_err_com is not None:
                print("ERROR:", mens_err_com)
        except TypeError as error:
            raise TypeError("ERROR [al llamar a comprobar()]:", error)
