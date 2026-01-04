'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 5 in num:
    num.remove(5)
else:
    print('Não ache o número 4')
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
#valores.append(5)
#valores.append(9)
#valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}! ', end='')
print('Cheguei ao final da lista.')'''

a = [1,2,3]
#b = a
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')