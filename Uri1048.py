"""Exemplo de Entrada	Exemplo de Saída
400.00
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %

800.01
Novo salario: 880.01
Reajuste ganho: 80.00
Em percentual: 10 %

2000.00
Novo salario: 2140.00
Reajuste ganho: 140.00
Em percentual: 7 %
"""
sal = float(input())
if 0 < sal <= 400:
    salnv = sal + (sal/100 * 15)
    print(f'Novo salario: {format(salnv, ".2f")}\nReajuste ganho: {format(salnv - sal,".2f")}\nEm percentual: 15 %')
elif 400 < sal <= 800:
    salnv = sal + (sal / 100 * 12)
    print(f'Novo salario: {format(salnv, ".2f")}\nReajuste ganho: {format(salnv - sal, ".2f")}\nEm percentual: 12 %')
elif 800 < sal <= 1200:
    salnv = sal + (sal / 100 * 10)
    print(f'Novo salario: {format(salnv, ".2f")}\nReajuste ganho: {format(salnv - sal, ".2f")}\nEm percentual: 10 %')
elif 1200 < sal <= 2000:
    salnv = sal + (sal / 100 * 7)
    print(f'Novo salario: {format(salnv, ".2f")}\nReajuste ganho: {format(salnv - sal, ".2f")}\nEm percentual: 7 %')
else:
    salnv = sal + (sal / 100 * 4)
    print(f'Novo salario: {format(salnv, ".2f")}\nReajuste ganho: {format(salnv - sal, ".2f")}\nEm percentual: 4 %')
