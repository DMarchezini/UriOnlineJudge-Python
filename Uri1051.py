"""Exemplos de Entrada	Exemplos de Saída
3002.00
R$ 80.36

1701.12
Isento

4520.00
R$ 355.60
"""
renda = float(input())
imposto = float()
if 0 <= renda <= 2000:
    print('Isento')
elif 2000 < renda <= 3000:
    imposto = (renda - 2000) / 100 * 8
    print(f'R$ {format(imposto, ".2f")}')
elif 3000 < renda <= 4500:
    imposto = renda - 3000
    imposto = imposto / 100 * 18 + 80
    print(f'R$ {format(imposto, ".2f")}')
elif renda > 4500:
    imposto = renda - 4500
    imposto = 350 + imposto / 100 * 28
    print(f'R$ {format(imposto, ".2f")}')
else:
    print('Erro')
