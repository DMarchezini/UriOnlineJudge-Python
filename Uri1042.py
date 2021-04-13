"""
Exemplo de Entrada	Exemplo de Saída
7 21 -14
-14
7
21

7
21
-14

-14 21 7
-14
7
21

-14
21
7
"""
info = input().split()
a, b, c = info
a = int(a)
b = int(b)
c = int(c)
lista = [a, b, c]
lista.sort()
for numero in lista:
    print(numero)
print('')
print(f'{a}\n{b}\n{c}')
