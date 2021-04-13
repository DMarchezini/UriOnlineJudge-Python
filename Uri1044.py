"""Exemplo de Entrada	Exemplo de Saída
6 24
Sao Multiplos

6 25
Nao sao Multiplos
"""
info = input().split()
a, b = info
a = int(a)
b = int(b)
if b % a == 0 or a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
