"""Exemplos de Entrada	Exemplos de Saída
25
100
5.50
NUMBER = 25
SALARY = U$ 550.00

1
200
20.50
NUMBER = 1
SALARY = U$ 4100.00

6
145
15.55
NUMBER = 6
SALARY = U$ 2254.75
"""
idfunc = int(input())
salario = format(int(input()) * float(input()), '.2f')
print(f'NUMBER = {idfunc}')
print(f'SALARY = U$ {salario}')
