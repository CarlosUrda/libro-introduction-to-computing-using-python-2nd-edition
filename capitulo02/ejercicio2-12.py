#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 12 del Capítulo 02
"""

def main():
	s1 = '-'
	s2 = '+'

	print(s1+s2)
	print(s1+s2+s1)
	print(s2+s1*2)
	print((s2+s1*2)*2)
	print(s2+(s1*2+s2)*10)
	print((s2+s1+s2*3+s1*2)*5)


if __name__ == "__main__" or __name__=="__console__":
	main()
