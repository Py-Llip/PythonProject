lista = []
cont = 0
while True:
    continu = ''
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    while continu not in ['S', 'N']:
        continu = str(input('Deseja continuar? [S,N] ')).upper().strip()[0]
        if continu not in ['S', 'N']:
            print('Dados inválidos, tente novamente:')
    if continu in 'N':
        break
print(f'Foram digitados {cont} números')
lista.sort(reverse=True)
print(f'A ordem decrescente da lista é {lista}')
if 5 in lista:
    print(f'o valor 5 está na lista')
else:
    print(f'O valor 5 NÃO está na lista')
print('Programa Finalizado')