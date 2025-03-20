'''
n = str(input('Digite uma expressão: '))
p1 = n.count('(')
p2 = n.count(')')
if p1 == p2:
    print('Expressão válida')
else:
    print('inválida')
cont1 = 0
cont2 = 0
n = str(input('Digite uma expressão: '))
for c in range(0, len(n)):
    print(n[c])
    if n[c] in ')':
        cont1 += 1
    elif n[c] in '(':
        cont2 += 1
if cont1 == cont2:
    print('Expressão válida')
else:
    print('Expressão inválida')'''
n = str(input('Digite uma expressão: '))
lista = []
for c in range(0, len(n)):
    if n[c] in '(':
        lista.append(n[c])
    elif n[c] in ')':
        if len(lista) > 0:
            lista.pop()
if len(lista) > 0:
    print('Expressão inválida')
else:
    print('Expressão válida')
