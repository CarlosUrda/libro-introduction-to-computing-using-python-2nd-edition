#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio alternativo de StackOverflow.
Crear un cuadro de Punnet con Tkinter
"""

import tkinter as tk
from tkinter import font


def tabla(punnett, combf, combm):
    """
    Imprimir un cuadro de Punnet.

    Argumentos:
        punnett: lista con los datos del contenido del cuadro.
        combf: lista con los datos de la cabecera (fila 0).
        combm: lista con los datos de la columna 0.
    """
    resultados = tk.Toplevel()
    frame = tk.Frame(resultados)
    ftabla, fbutton = font.Font(family="Open Sans", size=11),\
                      font.Font(family="Dubai Light", size=11)
    fila, columna, contadorpunnett = 0, 0, 0

    for fila in range(33):
        for columna in range(33):
            if fila == 0 and columna == 0:
                continue
            if fila == 0:
                texto = combf[columna-1]
            elif columna == 0:
                texto = combm[fila-1]
            else:
                texto = punnett[contadorpunnett]
                contadorpunnett += 1
            print(texto, end=" ")
            tk.Label(frame, font=ftabla,\
                     text=texto.grid(row=fila, column=columna))
        print("\n")


def main():
    """
    Función principal.
    """
    punnet = [2]*32*32
    combm = ["a"]*32
    combf = ["b"]*32
    #print(punnet,combm,combf)
    tabla(punnet, combf, combm)


if __name__ in ("__main__", "__console__"):
    main()
