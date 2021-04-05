"""Exemplo de Entrada	Exemplo de Saída
400
1 ano(s)
1 mes(es)
5 dia(s)

800
2 ano(s)
2 mes(es)
10 dia(s)

30
0 ano(s)
1 mes(es)
0 dia(s)
"""
dias = int(input())
anos = int(dias/365)
dias -= anos * 365
meses = int(dias/30)
dias -= meses * 30
print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')
