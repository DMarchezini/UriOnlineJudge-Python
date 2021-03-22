"""
Exemplos de Entrada	Exemplos de Saída
7 14 106
106 eh o maior

217 14 6
217 eh o maior
"""
valor = input().split(" ")
a, b, c = valor
maiorab = (int(a) + int(b) + abs(int(a) - int(b)))/2
maior = (int(maiorab) + int(c) + abs(int(maiorab) - int(c)))/2
print('%d eh o maior' %maior)
