"""
Exemplos de Entrada	Exemplos de Saída
3
VOLUME = 113.097

15
VOLUME = 14137.155

1523
VOLUME = 14797486501.627
"""
r = float(input())
volume = format(((4/3) * 3.14159) * r**3, '.3f')
print(f'VOLUME = {volume}')
