"""Exemplos de Entrada	Exemplos de Saída
5.0
7.1
MEDIA = 6.43182

0.0
7.1
MEDIA = 4.84091

10.0
10.0
MEDIA = 10.00000
"""
a = float(input())
b = float(input())
media = format(((a * 3.5) + (b * 7.5)) / 11, '.5f')
print(f'MEDIA = {media}')
