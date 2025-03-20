lista = [[],[],[]]
s = 0
sc = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l].append(int(input(f'Digite um número para [{l}, {c}]: ')))
        if lista[l][c] % 2 == 0:
            s += lista[l][c]
print(lista)
print('=-'*30)
for l in range(0, 3):
    sc += lista[l][2]
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
        if c == 0:
            maior = lista[1][c]
        elif lista[1][c] > maior:
            maior = lista[1][c]
    print()
print('=-'*30)
print(f'A soma dos valores pares é {s}\nA soma dos valores da terceira coluna é {sc}\nO maior valor da segunda linha é {maior}')
