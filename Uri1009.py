"""
Exemplos de Entrada	Exemplos de Saída
JOAO
500.00
1230.30
TOTAL = R$ 684.54

PEDRO
700.00
0.00
TOTAL = R$ 700.00

MANGOJATA
1700.00
1230.50
TOTAL = R$ 1884.58
"""
nome = input()
salario = format(float(input()) + ((float(input()) / 100) * 15), '.2f')
print(f'TOTAL = R$ {salario}')
