"""Exemplos de Entrada	Exemplos de Saída
5.0
6.0
7.0
MEDIA = 6.3

5.0
10.0
10.0
MEDIA = 9.0

10.0
10.0
5.0
MEDIA = 7.5
"""
a = float(input())
b = float(input())
c = float(input())
media = format((((2 * a) + (3 * b) + (5 * c)) / 10), '.1f')
print(f'MEDIA = {media}')
