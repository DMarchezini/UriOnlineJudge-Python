"""
Exemplos de Entrada	/ Exemplos de Saída
3.0 4.0 5.2
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000

12.7 10.4 15.2
TRIANGULO: 96.520
CIRCULO: 725.833
TRAPEZIO: 175.560
QUADRADO: 108.160
RETANGULO: 132.080
"""
valores = input().split(" ")
a, b, c = valores
triangulo = format((float(a) * float(c)) / 2, '.3f')
circulo = format(3.14159 * float(c)**2, '.3f')
trapezio = format((((float(a) + float(b)) * float(c))/2), '.3f')
quadrado = format(float(b)**2, '.3f')
retangulo = format(float(a) * float(b), '.3f')
print(f'TRIANGULO: {triangulo}\nCIRCULO: {circulo}\nTRAPEZIO: {trapezio}\nQUADRADO: {quadrado}\nRETANGULO: {retangulo}')
