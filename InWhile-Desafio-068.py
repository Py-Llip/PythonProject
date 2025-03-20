from random import randint
print('Par ou ímpar')
d = ''
cont = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    c = randint(1, 10)
    if (n + c) % 2 == 0:
        d = 'PAR'
    else:
        d = 'ÍMPAR'
    print(f'Você jogou {n} e o computador {c}. No total de {n + c} deu {d}')
    cont += 1
    if pi == 'P':
        if (n + c) % 2 == 0:
            print('Você Ganhou!')
        else:
            print('você perdeu.')
            print(f'Com {cont} tentativas!')
            break
    elif pi == 'I':
        if (n + c) % 2 == 0:
            print('Você perdeu.')
            print(f'Com {cont} tentativas!')
            break
        else:
            print('Você ganhou!')
    else:
        print('Dado inválido, tente novamente: ')
        cont -= 1
    print('Vamos jogar novamente: ')
