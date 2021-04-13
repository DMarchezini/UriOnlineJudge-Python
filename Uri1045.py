"""Exemplos de Entrada	Exemplos de Saída
7.0 5.0 7.0
TRIANGULO ACUTANGULO
TRIANGULO ISOSCELES

6.0 6.0 10.0
TRIANGULO OBTUSANGULO
TRIANGULO ISOSCELES

6.0 6.0 6.0
TRIANGULO ACUTANGULO
TRIANGULO EQUILATERO

5.0 7.0 2.0
NAO FORMA TRIANGULO

6.0 8.0 10.0
TRIANGULO RETANGULO
"""
info = input().split()
a, b, c = info
a = float(a)
b = float(b)
c = float(c)
lista = [a, b, c]
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]
if a > 0 and b > 0 and c > 0:
    if a == b or a == c or b == c:
        if a == b == c:
            if a**2 < (b**2 + c**2):
                print('TRIANGULO ACUTANGULO')
                print('TRIANGULO EQUILATERO')
            else:
                print('TRIANGULO EQUILATERO')
        elif a >= (b + c):
            print('NAO FORMA TRIANGULO')
            print('TRIANGULO ISOSCELES')
        elif a**2 == (b**2 + c**2):
            print('TRIANGULO RETANGULO')
            print('TRIANGULO ISOSCELES')
        elif a**2 > (b**2 + c**2):
            print('TRIANGULO OBTUSANGULO')
            print('TRIANGULO ISOSCELES')
        elif a**2 < (b**2 + c**2):
            print('TRIANGULO ACUTANGULO')
            print('TRIANGULO ISOSCELES')
    else:
        if a ** 2 < (b ** 2 + c ** 2):
            print('TRIANGULO ACUTANGULO')
        elif a >= (b + c):
            print('NAO FORMA TRIANGULO')
        elif a**2 == (b**2 + c**2):
            print('TRIANGULO RETANGULO')
        elif a**2 > (b**2 + c**2):
            print('TRIANGULO OBTUSANGULO')
        elif a**2 < (b**2 + c**2):
            print('TRIANGULO ACUTANGULO')
