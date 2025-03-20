'''for c in range(1, 11):
    print(c)
print('FIM')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    r = str(input('Quer continuar? [S/N]'))
print('FIM')'''

n = 1
par = impar =0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('FIM', par, impar)








