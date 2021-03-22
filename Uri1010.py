"""
Exemplos de Entrada	Exemplos de Saída
12 1 5.30
16 2 5.10
VALOR A PAGAR: R$ 15.50

13 2 15.30
161 4 5.20
VALOR A PAGAR: R$ 51.40

1 1 15.10
2 1 15.10
VALOR A PAGAR: R$ 30.20
"""
linha1 = input().split(" ")
linha2 = input().split(" ")
cod1, qtd1, valor1 = linha1
cod2, qtd2, valor2 = linha2
total = format(int(qtd1) * float(valor1) + int(qtd2) * float(valor2), '.2f')
print(f'VALOR A PAGAR: R$ {total}')
