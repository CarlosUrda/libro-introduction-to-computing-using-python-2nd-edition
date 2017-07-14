#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio realizado para Stack Overflow.
https://es.stackoverflow.com/questions/87037/list-index-out-of-range-python-3/87072#87072
"""

import random


def obtener_indices_mutables(tam_poblacion, tam_mutables):
    """
    Obtener la lista de índices de los individuos de la población de un
    tamaño determinado que podrán ser mutados.

    Argumentos:
        tam_poblacion: tamaño total de la población cuya parte podrá ser mutada.
        tam_mutables: tamaño de parte de la población que podrá ser mutada.

    Retorno:
        Lista de índices de los individuos que podrán mutar. Esta lista tiene
        un tamaño de tam_mutantes.
    """
    indices_poblacion = list(range(tam_poblacion))
    random.shuffle(indices_poblacion)
    return indices_poblacion[:tam_mutables]


def mutacion(poblacion, tam_reproductores, prob_mutacion, tam_genes):
    """
    Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca
    podría alcanzarse la solucion.

    Argumentos:
        poblacion: población a mutar los individuos que no se reproducen. Lista
        de listas donde cada elemento (individuo) de la lista principal
        contiene una lista con los valores por cada gen.
        tam_reproductores: número de individuos de la población que se
        reproducirán. Es decir, los padres.
        prob_mutacion: probabilidad de que un individo con posibilidad de ser
        mutado, mute.
        tam_genes: longitud del material genético de cada individuo.

    Retorno:
        Población con los individuos mutados.
    """
    #MUTACION UNIFORME

    tam_poblacion = len(poblacion)
    tam_mutables = tam_poblacion - tam_reproductores

    for i in obtener_indices_mutables(tam_poblacion, tam_mutables):
        if random.random() > prob_mutacion:
            continue

        punto = random.randint(0, tam_genes-1)
        valores = list(range(1, 9+1))
        valores.remove(poblacion[i][punto])
        poblacion[i][punto] = random.choice(valores)

    return poblacion


def main():
    """
    Función principal.
    """
    largo = 16 #La longitud del material genetico de cada individuo
    num = 22 #La cantidad de individuos que habra en la poblacion
    indAReproducir = 7 #Individuos elegidos para la reproduccion
    prob_mutacion = 0.2 #La probabilidad de que un individuo mute

    poblacion = [[1]*largo for i in range(num)]
    print(poblacion, "\n")

    poblacion = mutacion(poblacion, indAReproducir, prob_mutacion, largo)
    print(poblacion)


if __name__ in ("__main__", "__console__"):
    main()
