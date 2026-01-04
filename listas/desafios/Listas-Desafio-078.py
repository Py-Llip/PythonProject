lista = []
pm = []
pn = []
maior = menor = 0
for c in range(0,5):
    n = int(input(f'Digite um valor na posição {c} '))
    lista.append(n)
    if c == 0:
        menor = maior = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
#for i, v in enumerate(lista):
#    if v == maior:
#        pm.append(i)
#    elif v == menor:
#        pn.append(i)
for cont in range(0, len(lista)):
    if lista[cont] == maior:
        pm.append(cont)
    elif lista[cont] == menor:
        pn.append(cont)
print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições {pm}')
print(f'O menor valor digitado foi {menor} nas posições {pn}')


