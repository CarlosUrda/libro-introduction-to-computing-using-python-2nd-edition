#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 21 del Capítulo 02.
"""

def main():
	nombre = input("Introduce el nombre: ").strip()
	print("El nombre es:", nombre)	

	apellido = input("Introduce el apellido: ").strip()
	print("El apellido es:", apellido)	

	iniciales = (nombre[0]+apellido[0]).upper()	
	print("Las iniciales son:", iniciales)
	

if __name__ in ("__main__", "__console__"):
	main()
