from random import randint
lista = []
n = int(input('Quantos jogos quer? '))
for c in range(0, n):
    sublista = []
    while len(sublista) < 6:
        sort = randint(1, 60)
        if sort not in sublista:
            sublista.append(sort)
    lista.append(sublista)
    sublista.sort()
print('=-'*30)
for c in range(0, n):
    print(f'{lista[c]}')
