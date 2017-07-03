#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 22 del Capítulo 02.
"""

def main():
	while True:
		datos = input("Introduce la lista de números: ").strip()
		try:
			numeros = [int(n) for n in datos.split()]
		except Exception:
			print("Tienes que introducir números enteros separados por espacios.")
		else:
			break
			
	numeros.sort()	
	print("Lista de números introducida:", numeros)
	rango = max(numeros) - min(numeros)
	print("Rango:", rango)


if __name__ in ("__main__", "__console__"):
	main()
