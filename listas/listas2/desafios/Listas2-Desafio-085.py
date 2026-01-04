lista = [[], []]
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'A lista {lista} tem os fatores {lista[0]} pares e {lista[1]} ímpares')