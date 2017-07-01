#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 15 del Capítulo 02
"""

def main():
	p1 = "anachronistically"
	p2 = "counterintuitive"
	print("len(\"{}\") == 1 + len(\"{}\"): ".format(p1, p2), len(p1) == 1 + len(p2))

	p1 = "misinterpretation"
	p2 = "misrepresentation"
	print("\"{}\" < \"{}\": ".format(p1, p2), p1 < p2)

	p = "floccinaucinihilipilification"
	print("El cáracter 'e' no aparece en \"{}\": ".format(p1),  'e' in p)

	p1 = "counterrevolution"
	p2 = "counter"
	p3 = "resolution"
	print("len(\"{}\") == len(\"{}\") + len(\"{}\"): ".format(p1, p2, p3), len(p1) == len(p2)+len(p3))


if __name__=="__main__" or __name__=="__console__":
	main()
