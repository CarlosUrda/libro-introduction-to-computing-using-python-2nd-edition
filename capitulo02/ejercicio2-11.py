#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 11 del Capítulo 2
"""

def main():
	print(sum(range(-7,0)))

	alumnos_por_edad = {9: 17, 10: 24, 11: 21, 12: 27}
	alumnos = suma_edades = 0
	for edad in alumnos_por_edad:
		alumnos += alumnos_por_edad[edad]
		suma_edades += alumnos_por_edad[edad] * edad
	print(suma_edades / alumnos)

	print(2**-20)

	print(4356 // 61)

	print(4356 % 61)


if __name__ == '__main__' or __name__ == '__console__':
	main()
