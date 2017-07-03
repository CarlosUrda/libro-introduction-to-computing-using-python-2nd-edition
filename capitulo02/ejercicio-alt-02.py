#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio de StackOverflow

Obtener los índices de los elementos repetidos en una lista
"""

from collections import Counter
from collections import defaultdict

def main():
	lista = [1,2,3,4,4,3]
	counts_por_elem = Counter(lista)
	
	indices_por_elem = defaultdict(list)
	indices = []

	for indice, elem in enumerate(lista):
		if counts_por_elem[elem] > 1:
			indices.append(indice)
			indices_por_elem[elem].append(indice)
		
	print(indices_por_elem)
	print(indices)
	

if __name__ in ("__main__", "__console__"):
	main()
