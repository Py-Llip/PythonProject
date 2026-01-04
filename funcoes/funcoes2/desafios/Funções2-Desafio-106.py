from time import sleep

def tytle(titulo, passo1=0):
    espacamento = len(titulo)+10
    if passo1 == 1:
        print('\033[4;36;45m*' * espacamento)
    elif passo1 == 0:
        print('\033[1;97;47m*' * espacamento)
    else:
        print('\033[1;97;41m*' * espacamento)
    print(f'{titulo:^{espacamento}}')
    print('*' * espacamento)


def search(txt):
    print('\033[0;30;107m', end='')
    help(txt)


while True:
    tytle('Sistema de Ajuda PyHelp', passo1=0)
    valor = str(input('\033[mFunção ou Biblioteca > ')).lower().strip()
    if valor == 'fim':
        break
    tytle(f'Acessando o manual do comando "{valor}"', passo1=1)
    sleep(2)
    search(valor)
    sleep(1)
tytle('Até logo!', passo1=2)
