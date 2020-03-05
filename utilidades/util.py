#/usr/bin/env python3
#!coding=utf-8

"""
Módulo con utilidades para los ejercicios del libro.
"""

import collections as collec
import numbers as num
import re



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

    Notas:
        En la documentación oficial de Python dice que la única forma de saber
        si un objeto es iterable es llamar a iter(). Pero también dice que un
        iterable es un objeto defindo con el método __iter__() o el método
        __getitem__(). NO confundir con la clase abstracta Iterable, la cual
        solo tiene como condición tener un método __iter__()
    """
    #return hasattr(objeto, "__getitem__") or hasattr(objeto, "__iter__")
    try:
        iter(objeto)
    except Exception:
        return False

    return True



def es_subiterable(subiter, superiter):
    """
    Comprueba si todos los elementos de un objeto iterable (subiterable) están
    dentro de otro iterable.

    Argumentos:
        - subiter: iterable a comprobar sus elementos dentro de otra iterable.
        - superiter: iterable a comprobar si todos los elementos de otro
        iterable están dentro de él.

    Excepciones:
        - TypeError al no poder convertir los argumentos a conjuntos porque no
        son iterables.
    """
    try:
        return set(subiter) <= set(superiter)
    except Exception as error:
        raise TypeError("ERROR: no se pudo convertir argumentos a conjuntos.",\
                        error)



def eliminar_repes(iterable):
    """
    ELimina las repeticiones de elementos de un iterable obteniendo los
    elementos no repetidos en una nueva lista. Los elementos del iterable pueden
    ser mutables.

    Argumentos:
        - iterable: iterable de elementos mutables o no.

    Excepciones:
        - TypeError: si el argumento repes no es un objeto iterable.

    Retorno:
        Devuelve una nueva lista con los elementos no repetidos (primera vez que
        aparecen) de un iterable en el orden original.

    Notas:
        Se podría optimizar esta función para los siguientes casos:
            - Si el iterable es una colección mutable se pueden eliminar los
            elementos repetidos en la propia colección sin necesidad de crear
            una lista nueva.
    """
    if not es_iterable(iterable):
        raise TypeError(f"El argumento 'iterable' {iterable} no es iterable.")

    lista = []
    for elem in iterable:
        if elem not in lista:
            lista.append(elem)

    return lista



def eliminar_repes_inm(iterable, orden=True):
    """
    ELimina las repeticiones de elementos inmutables de un iterable obteniendo
    los elementos no repetidos en una nueva lista. Utiliza la inmutabilidad de
    todos los elementos para realizar la eliminación más rápidamente.

    Argumentos:
        - iterable: iterable con todos los elementos inmutables.
        - orden: flag para indicar si la lista obtenida mantiene el orden de los
        elementos del iterable original. Si obliga a mantener el orden se
        ejecuta más rápido.

    Excepciones:
        - TypeError: si el argumento repes no es un objeto iterable.
        - TypeError: si alguno de los elementos del iterable es mutable.

    Retorno:
        Devuelve una nueva lista con los elementos no repetidos de un iterable.
        Si orden es True, los elementos no repetidos aparecen en el ordenar
        original. Si orden es False, los elementos no repetidos pueden aparecer
        en cualquier orden.

    Notas:
        Se podría optimizar esta función para los siguientes casos:
            - Si el iterable es una colección mutable se pueden eliminar los
            elementos repetidos en la propia colección sin necesidad de crear
            una lista nueva.
    """
    if not es_iterable(iterable):
        raise TypeError(f"El argumento 'iterable' {iterable} no es iterable.")

    try:
        if not orden:
            return list(set(iterable))

        lista = []
        repes = {}
        for elem in iterable:
            if not repes.get(elem, False):
                repes[elem] = True
                lista.append(elem)
    except TypeError as error:
        raise TypeError("Los elementos de 'iterable' no son inmutables", error)

    return lista



def cadena_a_lista(cadena, separador=None, flags=0):
    """
    Convierte una cadena con grupos de caracteres delimitados por un separador
    a una lista donde cada elemento es cada grupo de caracteres extraído.

    Argumentos:
        - cadena: cadena cuyos caracteres separados por separador serán los
        elementos de la lista obtenida.
        - separador: subcadena a usar como separador de cada uno de los
        elementos de la cadena de entrada. Si None se separan por espacios
        eliminando estos espacios.
        - flags: bits que activan modificaciones a la lista generada:
            0bxxxxxx00: Mantener las mayúsculas y minúsculas como están.
            0bxxxxxx01: Capitalizar cada elemento de la lista resultante.
            0bxxxxxx10: Convertir a minúsculas todos los elementos de la lista.
            0bxxxxxx11: Convertir a mayúsculas todos los elementos de la lista.
            0bxxxxx0xx: Mantener las repeticiones de elementos en la lista.
            0bxxxxx1xx: Eliminar las repeticiones de elementos en la lista.
            0bxxx00xxx: No ordenar los elementos de la lista.
            0bxxx01xxx: Ordenar los elementos de la lista en orden ascendente.
            0bxxx10xxx: Ordenar los elementos de la lista en orden descendente.
            0bxxx11xxx: Invertir el orden inicial de los elementos de la lista.
            0bxx0xxxxx: Mantener espacios en blanco envolviendo cada elemento.
            0bxx1xxxxx: Eliminar espacios en blanco envolviendo cada elemento.
            0bx0xxxxxx: Mantener elementos vacíos.
            0bx1xxxxxx: Eliminar elementos vacíos.

    Retorno:
        Lista donde cada elemento es cada una de las subcadenas separadas por
        separador en la cadena de entrada. El separador y los espacios en blanco
        alrededor de cada subcadena no aparecen en cada elemento de la lista.

    Excepciones:
        - ValueError si el valor de la cadena separador es incorrecto ("").
        - TypeError si los argumentos tiene un tipo de dato incorrecto.

    Notas:
        En lugar de pasar un argumento flags con los bits activados, pasar cada
        opción en un argumento distinto y recibirlo como un diccionario: kargs.
        Aunque esto hay que verlo bien, es solo una sugerencia.
    """
    # Comprobación de los argumentos
    if not isinstance(cadena, str):
        raise TypeError("El argumento cadena no es de tipo str")
    if separador is not None and not isinstance(separador, str):
        raise TypeError("El argumento separador no es de tipo str")
    if not isinstance(flags, int):
        raise TypeError("El argumento flags no es de tipo int")

    flags_base = {"capital": 0b01, "mayusc": 0b11, "minusc": 0b10,
                  "repet": 0b100, "invert": 0b11000, "ascen": 0b01000,
                  "descen": 0b10000, "blanco": 0b100000, "vacio": 0b1000000}

    # Eliminación de los caracteres en blanco alrededor de cada elemento.
    if flags & flags_base["blanco"]:
        cadena = re.sub(rf"\s*({separador})\s*", rf"\1", cadena.strip())

    # Modificación de mayúsculas/minúsculas.
    flags_case = flags & flags_base["mayusc"]
    if flags_case == flags_base["mayusc"]:
        cadena = cadena.upper()
    elif flags_case == flags_base["minusc"]:
        cadena = cadena.lower()
    elif flags_case == flags_base["capital"]:
        cadena = re.sub(rf"^([^{separador}]+)",
                        lambda x: x.group(1).capitalize(), cadena)
        cadena = re.sub(rf"({separador})([^{separador}]+)",
                        lambda x: x.group(1)+x.group(2).capitalize(), cadena)

    try:
        lista = cadena.split(separador)
    except ValueError as error:
        raise ValueError("Valor de la cadena separador incorrecto", error)

    # Eliminación de los elementos vacíos de la lista.
    if flags & flags_base["vacio"]:
        lista = list(filter(bool, lista))

    flags_orden = flags & flags_base["invert"]
    es_invertir = flags_orden == flags_base["invert"]

    # Eliminación de las repeticiones de los elementos
    if flags & flags_base["repet"]:
        lista = eliminar_repes_inm(lista, es_invertir or not flags_orden)

    # Modificación del orden de los elementos en la lista.
    if es_invertir:
        lista.reverse()
    elif flags_orden:
        lista.sort(reverse=bool(flags_base["descen"] & flags_orden))

    return lista



def obtener_dato(mensaje, convertir=None, es_correcto=None, fin=None,\
                 mens_err_conv=None, mens_err_corr=None):
    """
    Lee una cadena por teclado y la convierte a otro tipo de dato pasándola a
    la función convertir(). El valor obtenido en la conversión se comprueba
    pasándolo a la función es_correcto().

    Si convertir() no convierte la cadena correctamente (lanza excepción
    ValueError o TypeError), o es_correcto() comprueba que el valor obtenido
    de la conversión no es correcto (devuelve False), se seguirá pidiendo una
    cadena por teclado hasta que se cumplan estas dos condiciones.

    Argumentos:
        - mensaje: mensaje a mostrar antes de introducir el dato por teclado.
        - convertir: función usada para convertir la cadena introducida y
        obtener el tipo de dato deseado. Debe lanzar una excepción ValueError o
        TypeError si la cadena no se ha podido convertir al tipo de dato
        correcto. Si es None la cadena leída por teclado no se convierte.
        - es_correcto: función que comprueba si el valor del dato obtenido en la
        conversión cumple las condiciones deseadas. Si es None, no se realiza
        ninguna comprobación del dato. Devuelve True o False si el dato cumple o
        no las condiciones.
        - fin: cadena a comparar con la cadena leída (sin convertir aún) para
        salir de la función sin obtener ningún dato. Si es igual a la cadena
        leída por teclado se lanza la excepción EOFError.
        - mens_err_conv: mensaje de error a mostrar en caso de que no se pueda
        convertir el dato (ValueError o SyntaxError). Si el último carácter es
        ':' se imprime junto con el mensaje interno de la excepción generada por
        convertir(). Si es None, no se imprime ningún mensaje (ni el interno de
        la excepción).
        - mens_err_corr: mensaje de error a mostrar en caso de no cumplirse las
        condiciones de la función es_correcto(). Si es None, no se imprime
        ningún mensaje.

    Retorno:
        Dato introducido por teclado ya convertido y pasado la comprobación.

    Excepciones:
        - Lanza TypeError si alguno de los parámetros tiene un tipo incorrecto.
        - Si la llamada a convertir() genera alguna excepción distinta a
        ValueError o TypeError la función termina lanzando dicha excepción.
        - Si la llamada a es_correcto() genera alguna excepción la función
        termina y lanza dicha excepción.
        - Lanza EOFError si recibe una cadena en 'fin' y coincide con la cadena
        leída por teclado.

    Notas
        Los parámetros convertir y es_correcto actuarán como funciones sobre los
        datos introducidos por teclado. Tener cuidado de no pasar funciones
        como eval.
    """
    # Comprobación de los argumentos
    if not isinstance(mensaje, str):
        raise TypeError("El argumento 'mensaje' no es de tipo str")
    if convertir is not None and not callable(convertir):
        raise TypeError("El argumento 'convertir' no es una función.")
    if es_correcto is not None and not callable(es_correcto):
        raise TypeError("El argumento 'es_correcto' no es una función.")
    if fin is not None and not isinstance(fin, str):
        raise TypeError("El argumento 'fin' no es de tipo str")
    if mens_err_conv is not None and not isinstance(mens_err_conv, str):
        raise TypeError("El argumento 'mens_err_conv' no es de tipo str")
    if mens_err_corr is not None and not isinstance(mens_err_corr, str):
        raise TypeError("El argumento 'mens_err_corr' no es de tipo str")

    while True:
        dato = input(mensaje)

        # Comprobación del fin de la lectura.
        if fin is not None and dato.strip() == fin.strip():
            raise EOFError(f"Cadena fin de lectura {fin} introducida")

        # Conversión de la cadena leída.
        try:
            if convertir is not None:
                dato = convertir(dato)
        except (ValueError, TypeError) as error:
            if mens_err_conv is not None:
                mens_err_conv = mens_err_conv.strip()
                print("ERROR:", mens_err_conv,\
                      '['+error+']' if mens_err_conv[-1]==':' else "")
            continue

        # Comprobación de valor de datos correctos.
        if es_correcto is not None and not es_correcto(dato):
            if mens_err_corr is not None:
                print("ERROR:", mens_err_corr.strip())
            continue

        return dato
