#!/usr/bin/env python3
#coding=utf-8

"""
Ejercicio 14 del Capítulo 02
"""

def main():
	s = input("Introduce una cadena: ")
	print("Primer carácter de \"{}\" es 'g': {}".format(s, s[0]=='g'))
	print("Séptimo carácter de \"{}\" es 'g': {}".format(s, s[6]=='g'))
	print("Primeros dos caracteres de \"{}\" son 'ga': {}".format(s, s[0:2]=="ga"))
	print("Penúltimo carácter de \"{}\" es 'x': {}".format(s, s[-2]=='x'))
	print("El carácter a mitad de \"{}\" es 'd': {}".format(s, s[len(s)//2]=='d'))
	print("El primer y último carácter \"{}\" son iguales: {}".format(s, s[0]==s[-1]))
	print("Los cuatro últimos caracteres de \"{}\" son \"tion\": {}".format(s, s[-4:]=="tion"))


if __name__=="__main__" or __name__=="__console__":
	main()
