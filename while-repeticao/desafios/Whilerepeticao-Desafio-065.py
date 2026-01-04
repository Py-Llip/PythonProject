cont = 0
soma = 0
fechar = 1
maior = 0
menor = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número para saber a média:'))
    soma += n
    if n != 0:
        cont += 1
    continuar = str(input('Deseja continuar?[S,N]: ')).strip().upper()[0]
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if continuar not in 'SsNn':
        continuar = 'S'
        print('Dado inválido')
media = soma / cont
print('A média foi {:.2f} e o maior entre eles foi {} e p menor foi {}'.format(media, maior, menor))