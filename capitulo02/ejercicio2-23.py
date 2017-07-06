#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 23 del Capítulo 02.
"""

def main():
	mesesL = ["Ene", "Feb", "Mar", "May"] 
	mesesT = ("Ene", "Feb", "Mar", "May") 

	mesesL.insert(mesesL.index("May"), "Abr")
	print(mesesL)

	mesesL.append("Jun")
	print(mesesL)

	mesesL.pop()
	print(mesesL)

	del mesesL[1]
	print(mesesL)

	mesesL.reverse()
	print(mesesL)

	mesesL.sort()
	print(mesesL)



if __name__ in ("__main__", "__console__"):
	main()
