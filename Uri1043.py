"""Exemplo de Entrada	Exemplo de Saída
6.0 4.0 2.0

Area = 10.0

6.0 4.0 2.1

Perimetro = 12.1
"""
info = input().split()
a, b, c = info
a = float(a)
b = float(b)
c = float(c)
if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print(f'Perimetro = {format((a+b+c),".1f")}')
else:
    print(f'Area = {format(((a + b) / 2) * c)}')
