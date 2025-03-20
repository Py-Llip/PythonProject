k = 0
cont = 0
pares = []
valor = (int(input('Digite um valor: ')),int(input('Digite outro valor: ')),int(input('Digite outro valor: ')),int(input('Digite outro valor: ')))
for c in range(0,4):
    if valor[c] % 2 == 0:
        pares.append(valor[c])
    if valor[c] == 3:
        k = valor.index(3)+1
print(f'O valor 9 apareceu {valor.count(9)} vez(es)\nNa pisição {k}° foi digitado o valor 3\nOs números pares foram {pares}')
