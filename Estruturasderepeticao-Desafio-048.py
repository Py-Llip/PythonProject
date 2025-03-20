s = 0
cont = 0
contr = 0
for c in range(1, 501,2):
    if c % 3 == 0:
        s += c
        cont = cont + 1
    contr = contr + 1
print('Entre 1 até 500 existe {} números ímpares e sendo múltiplos de 3 existem {} númenos sendo cada valor somado seja {} dentre eles'.format(contr, cont, s))

