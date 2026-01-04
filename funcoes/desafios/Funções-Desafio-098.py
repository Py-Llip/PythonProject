from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    cont = i
    if p == 0:
        p = 1
    if cont <= f:
        while cont <= f:
            print(cont, end=' ')
            cont += p
            sleep(0.3)
    else:
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.3)
    print('FIM')

contador(1, 10, 1)
contador(10, 1, 1)
a = int(input('iníco: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)


