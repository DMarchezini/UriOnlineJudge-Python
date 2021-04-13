"""Exemplo de Entrada	Exemplo de Saída
16 2
O JOGO DUROU 10 HORA(S)

0 0
O JOGO DUROU 24 HORA(S)

2 16
O JOGO DUROU 14 HORA(S)
"""
entrada = input().split()
a, b = entrada
a = int(a)
b = int(b)
if a == b:
    print('O JOGO DUROU 24 HORA(S)')
elif a > b:
    print(f'O JOGO DUROU {(24 - a) + b} HORA(S)')
else:
    print(f'O JOGO DUROU {b - a} HORA(S)')
