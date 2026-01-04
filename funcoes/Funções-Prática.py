'''def soma(a, b): <---- parametro
    s = a + b
    print(s)


soma(a=4, b=5)
soma(7, 5)
soma(4, 2)

def soma(a, b):
    print(f'O A = {a} e o B = {b}')
    s = a + b
    print(s)


soma(b=4, a=5)
soma(7, 5)
soma(4, 2)
def contador(*num):
#    print(num) # cria tuplas
    for valor in num:
        print(valor, end=' ')
    print('FIM')
    final = len(num)
    print(final)


contador(3,5,2,6)
contador(2,3)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
   # print(lst)


valores = [1,2,3]
dobra(valores)
print(valores)'''

def soma(*num):
    s = 0
    for valor in num:
        s += valor
    print('Somando temos', s)


soma(2,3,2,4,5)
soma(1,0,0,3)
