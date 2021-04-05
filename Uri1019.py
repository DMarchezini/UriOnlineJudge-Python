"""Exemplo de Entrada	Exemplo de Saída
556
0:9:16

1
0:0:1

140153
38:55:53
"""

segundos = int(input())
minutos = int(segundos/60)
segundos -= minutos*60
horas = int(minutos/60)
minutos -= horas*60
print(f'{horas}:{minutos}:{segundos}')
