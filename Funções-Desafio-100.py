from random import randint
from time import sleep


def sorteia(nums):
    print('Sorteando 5 valores da lista:')
    sleep(2)
    ter = 0
    while ter < 5:
        ter += 1
        nums.append(randint(0, 10))
    for v in nums:
        print(v, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


num = list()
sorteia(num)
somapar(num)


