"""
Exemplo de Entrada	Exemplo de Saída
1.0 7.0
5.0 9.0
4.4721

-2.5 0.4
12.1 7.3
16.1484

2.5 -0.4
-12.2 7.0
16.4575
"""
import math
p1 = input().split(" ")
p2 = input().split(" ")
x1, y1 = p1
x2, y2 = p2
res = format(math.sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2), '.4f')
print(res)
