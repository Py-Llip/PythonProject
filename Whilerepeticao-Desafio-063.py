print('Sequencia de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
s = n1 + n2
cont = 3
print(n1,n2,'', end='')
# 1+ 1 = 2, 1+2 = 3, 2 + 3 = 5
while cont <= n:
    print(s,'', end='')
    cont += 1
    n1 = n2
    n2 = s
    s = n1 + n2
print('FIM')



