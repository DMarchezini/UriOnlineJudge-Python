"""Exemplos de Entrada	Exemplos de Saída
vertebrado
mamifero
onivoro
homem

vertebrado
ave
carnivoro
aguia

invertebrado
anelideo
onivoro
minhoca
"""
i1 = input()
i2 = input()
i3 = input()
if i1 == 'vertebrado' and i2 == 'ave' and i3 == 'carnivoro':
    print('aguia')
elif i1 == 'vertebrado' and i2 == 'ave' and i3 == 'onivoro':
    print('pomba')
elif i1 == 'vertebrado' and i2 == 'mamifero' and i3 == 'herbivoro':
    print('vaca')
elif i1 == 'vertebrado' and i2 == 'mamifero' and i3 == 'onivoro':
    print('homem')
elif i1 == 'invertebrado' and i2 == 'inseto' and i3 == 'hematofago':
    print('pulga')
elif i1 == 'invertebrado' and i2 == 'inseto' and i3 == 'herbivoro':
    print('lagarta')
elif i1 == 'invertebrado' and i2 == 'anelideo' and i3 == 'hematofago':
    print('sanguessuga')
elif i1 == 'invertebrado' and i2 == 'anelideo' and i3 == 'onivoro':
    print('minhoca')
else:
    print('erro')
