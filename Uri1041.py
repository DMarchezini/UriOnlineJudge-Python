"""Exemplo de Entrada	Exemplo de Saída
4.5 -2.2
Q4

0.1 0.1
Q1

0.0 0.0
Origem
"""
dados = input().split(' ')
x, y = dados
x = float(x)
y = float(y)
if x == 0 and y == 0:
    print('Origem')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x != 0 and y == 0:
    print('Eixo X')
elif x > 0:
    if y > 0:
        print('Q1')
    else:
        print('Q4')
else:
    if y > 0:
        print('Q2')
    else:
        print('Q3')
