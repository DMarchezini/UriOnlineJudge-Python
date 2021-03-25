"""
Exemplo de Entrada	Exemplo de Saída
500
35.0
14.286 km/l

2254
124.4
18.119 km/l

4554
464.6
9.802 km/l
"""
distancia = int(input())
combustivel = float(input())
media = format(distancia/combustivel, '.3f')
print(f'{media} km/l')
