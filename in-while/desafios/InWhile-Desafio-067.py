cont = m = n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while cont <= 10:
        m = n * cont
        print(f' {n} * {cont} = {m}')
        cont += 1
    if cont > 10:
        cont = 0
print('Processo Finalizado.')

