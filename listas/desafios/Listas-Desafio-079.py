lista = []
while True:
    continu = ''
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado, apagado.')
    while continu not in ['S','N']:
        continu = str(input('Deseja continuar? [S,N] ')).upper().strip()[0]
        if continu not in 'NS':
            print('Dado inválido, tente novamente.')
    if continu == 'N':
        break
lista.sort()
print(f'A lista de todos os valores é {lista}')



