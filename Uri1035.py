"""
Exemplo de Entrada	Exemplo de Saída
5 6 7 8
Valores nao aceitos

2 3 2 6
Valores aceitos
"""
entrada = input().split(" ")
a, b, c, d = entrada
if int(b) > int(c) and int(d) > int(a) and (int(c) + int(d)) > (int(a) + int(b)) and int(c) > 0 and int(d) > 0 and \
        int(a) % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
