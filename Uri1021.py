"""Exemplo de Entrada	Exemplo de Saída
576.73
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01

4.00
NOTAS:
0 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
2 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
0 moeda(s) de R$ 0.01

91.01
NOTAS:
0 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
2 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
1 moeda(s) de R$ 0.01
"""
valor = float(input())
if 0 <= valor <= 1000000.00:
    n100 = int(valor / 100)
    valor -= n100 * 100
    n50 = int(valor / 50)
    valor -= n50 * 50
    n20 = int(valor / 20)
    valor -= n20 * 20
    n10 = int(valor / 10)
    valor -= n10 * 10
    n5 = int(valor / 5)
    valor -= n5 * 5
    n2 = int(valor / 2)
    valor -= n2 * 2
    m1 = int(valor / 1)
    valor -= m1 * 1
    m50 = int(valor / 0.5)
    valor -= m50 * 0.5
    m25 = int(valor / 0.25)
    valor -= m25 * 0.25
    m10 = int(valor / 0.1)
    valor -= m10 * 0.1
    m5 = int(valor / 0.05)
    valor -= m5 * 0.05
    m01 = int(valor / 0.01)
    print(f'NOTAS:\n{n100} nota (s) de R$ 100.00\n{n50} nota (s) de R$ 50.00\n{n20} nota  (s) de R$ 20.00\n{n10} nota (s) de '
          f'R$ 10.00\n{n5} nota (s) de R$ 5.00\n{n2} nota (s) de R$ 2.00')
    print(f'MOEDAS:\n{m1} moeda (s) de R$ 1.00\n{m50} moeda (s) de R$ 0.50\n{m25} moeda (s) de R$ 0.25\n{m10} moeda (s) '
          f'de R$ 0.10\n{m5} moeda (s) de R$ 0.05\n{m01} moeda (s) de R$ 0.01')
else:
    print('ERRO')
