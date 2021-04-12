"""Exemplo de Entrada	Exemplo de Saída
2.0 4.0 7.5 8.0
6.4
Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9

2.0 6.5 4.0 9.0
Media: 4.8
Aluno reprovado.

9.0 4.0 8.5 9.0
Media: 7.3
Aluno aprovado.
"""
notas = input().split(' ')
n1, n2, n3, n4 = notas
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = float(format(((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10, '.1f'))
if 5 <= media < 6.9:
    notaexame = float(input())
    print(f'Media: {media}')
    print('Aluno em exame.')
    print(f'Nota do exame: {notaexame}')
    res = float(format((media + notaexame) / 2, '.1f'))
    if res >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {res}')
elif media >= 7:
    print(f'Media: {media}')
    print('Aluno aprovado.')
else:
    print(f'Media: {media}')
    print('Aluno reprovado.')
