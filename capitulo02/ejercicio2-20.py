#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 20 del Capítulo 02.
"""

def main():
	while True:
		s = input("Introduce una cadena de 3 letras: ").strip()
		if len(s) == 3:
			break
	
	print("La cadena introducida es:", s)	
	
	print("La cadena al revés es:", s[-1::-1])


if __name__ in ("__main__", "__console__"):
	main()
