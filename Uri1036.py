"""
Exemplos de Entrada	Exemplos de Saída
10.0 20.1 5.1
R1 = -0.29788
R2 = -1.71212

0.0 20.0 5.0
Impossivel calcular

10.3 203.0 5.0
R1 = -0.02466
R2 = -19.68408

10.0 3.0 5.0
Impossivel calcular
"""
variaveis = input().split(" ")
a, b, c = variaveis
a = float(a)
b = float(b)
c = float(c)
if a == 0 or (b ** 2 - (4*a*c)) < 0:
    print('Impossivel calcular')
else:
    R1 = (- b + (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
    R2 = (- b - (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
    print(f'R1 = {format(R1, ".5f")}\nR2 = {format(R2, ".5f")}')
