print('\033[34m-=\033[m'*12)
print('\033[31mÍndice de Massa Corpórea\033[m')
print('\033[34m-=\033[m'*12)
p = float(input('Digite seu peso: Kg '))
a = float(input('Digite sua altura: m '))
imc = p // a**2
print('Imc {}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
