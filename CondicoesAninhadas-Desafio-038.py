n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
if n1 > n2:
    print('O número: {} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('O número: {} é menor que {}'.format(n1, n2))
else:
    print('O valor {} e {} é o mesmo'.format(n1, n2))

