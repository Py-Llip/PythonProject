n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
c = (n1 + n2)/2
if c < 5.0:
    print('Reprovado com média {}'.format(c))
elif c >= 5.0 and c <= 6.9:
    print('Recuperação com média {}'.format(c))
else:
    print('Aprovado com média {}'.format(c))
