lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    d = ''
    while d not in ['S', 'N']:
        d = str(input('continuar[S,N]: ')).strip().upper()[0]
        if d not in ['S', 'N']:
            print('Tente novamente, dados inválidos.')
    if d in 'N':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print(f'A lista completa {lista}\n, par {par}\n, ímpar {impar}')

