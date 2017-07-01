#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 13 del Capítulo 03
"""

def main():
	s = "abcdefghijklmnopqrstuvwxyz"
	print(s[0])
	print(s[s.find('c')])
	print(s[-1])
	print(s[-2])
	print(s[s.index('q')])


if __name__=="__main__" or __name__=="__console__":
	main()
