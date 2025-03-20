print('MERCADÂO DO BARATO')
tot = 0
contp = 0
menor = 0
cont = 0
barato = ''
while True:
    continuar = ' '
    cont += 1
    produto = str(input('Digite um Produto: '))
    preco = float(input('Digite o preço deste Produto: '))
    tot += preco
    if preco > 1000:
        contp += 1
    if cont == 1:
        menor = preco
        barato = produto
    if preco < menor:
        menor = preco
        barato = produto
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S,N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total a ser pago é de R${tot}\nExistem {contp} produtos a cima de R$1000\nE o produto mais barato é {barato} que custa R${menor}')
