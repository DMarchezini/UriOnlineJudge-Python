"""Exemplo de Entrada	Exemplo de Saída
3 2
Total: R$ 10.00

4 3
Total: R$ 6.00

2 3
Total: R$ 13.50
"""
info = input().split(' ')
cod, qtd = info
cod = int(cod)
qtd = int(qtd)
valores = [(1, 4), (2, 4.5), (3, 5), (4, 2), (5, 1.5)]
for valor in valores:
    if valor[0] == cod:
        total = valor[1] * qtd
        print(f'Total: R$ {format(float(total), ".2f")}')
