lista = []
cont = maior = menor = 0
listamn = []
listann = []
nomem = nomen = ''
while True:
    n = str(input('Digite o nome: '))
    cont += 1
    i = float(input('Digite seu peso: '))
    lista.append([n, i])
    continu = ''
    while continu not in ['S', 'N']:
        continu = str(input('Continuar [S,N]: ')).strip().upper()[0]
        if continu not in ['S', 'N']:
            print('Tente novamente:')
    if continu == 'N':
        break
print(f'Entre', end='')
for c in range(0, len(lista)):
    print(f' {lista[c][0]}', end='')
    if c == len(lista)-1:
        print('. ')
    else:
        print(', ', end='')
print(f'Com os pesos respectivamente', end='')

for c in range(0, len(lista)):
    print(f' {lista[c][1]}', end='')
    if c == len(lista)-1:
        print('. ')
    else:
        print(', ', end='')
    if c == 0:
        maior = lista[c][1]
        menor = lista[c][1]
        nomem = lista[c][0]
        nomen = lista[c][0]
    elif lista[c][1] > maior:
        maior = lista[c][1]
        nomem = lista[c][0]
    elif lista[c][1] < menor:
        menor = lista[c][1]
        nomen = lista[c][0]
for o in range(0, len(lista)):
    if maior == lista[o][1]:
        listamn.append(lista[o][0])
    if menor == lista[o][1]:
        listann.append(lista[o][0])
print(f'Foram cadastradas {cont} pessoas.')
print(f'As pessoas mais pesadas foram {listamn} com {maior} de peso todos')
print(f'As pessoas mais leves fora {listann} com {menor} de peso todos')
