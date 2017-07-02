#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 19 del Capítulo 02
"""

def main():
	answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
	print("answers:", answers)

	numYes = answers.count('Y')
	print("Número de 'Y'es:", numYes)

	numNes = answers.count('N')
	print("Número de 'N'es:", numNes)

	percentYes = numYes * 100 / len(answers)
	print("Porcentaje de 'Y':", percentYes)

	answers.sort()
	print("answers ordenada:", answers)

	f = answers.index('Y')
	print("Índice de primera ocurrencia de 'Y':", f)

if __name__ in ("__main__", "__console__"):
	main()
