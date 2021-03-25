"""Exemplo de Entrada	Exemplo de Saída
576
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

11257
11257
112 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
0 nota(s) de R$ 1,00

503
503
5 nota(s) de R$ 100,00
0 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
0 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
"""
original_x = 576
x = original_x
notas = [100, 50, 20, 10, 5, 2, 1]
results = []
if 0 < x < 1000000:
    for nota in notas:
        nota_amount = x // nota
        x -= nota_amount * nota
        results.append(nota_amount)

    print(original_x)
    for res, nota in zip(results, notas):
        print(f"{res} nota(s) de R$ {nota},00")
else:
    print('Erro')
