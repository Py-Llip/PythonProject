from time import sleep
def maior(*num):
    print('-'*30)
    print('Analisando os valores passados...')
    sleep(3)
    for v in num:
        print(v, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    maiorn = 0
    for e, c in enumerate(num):
        if e == 0:
            maiorn = c
        else:
            if maiorn < c:
                maiorn = c
    print(f'O maior valor informado foi {maiorn}')
maior(1,6,3,9,2,5,10,9)
maior(4,7,0)
maior(6)
maior()
print('-'*30)