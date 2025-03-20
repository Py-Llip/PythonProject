import math
q = str(input('Digite 1 se quer a conversão em binário\nDigite 2 para octal\nDigite 3 para hexadecimal\n: '))
n = int(input('Digite um número: '))
if q == '1':
    print(bin(n)[2:])
elif q == '2':
    print(oct(n)[2:])
elif q == '3':
    print(hex(n)[2:])
else:
    print('Inexistente')




