r1 = float(input('Coloque o comprimento da primeira reta: '))
r2 = float(input('Coloque o comprimento da segunda reta: '))
r3 = float(input('Coloque o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('É possivel formar um triangulo')
    if r1 == r2 == r3:
        print('E é um Equilátero')
    if r1 == r2 or r1 == r3 or r2 == r3:
        print('E é um Isósceles')
    else:
        print('E é um Escaleno')
else:
    print('Não é um triangulo')