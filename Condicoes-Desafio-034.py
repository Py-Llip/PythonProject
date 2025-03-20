salario = float(input('Qual o seu salário? '))
c = salario * 10 / 100
#o = salario + c
q = salario * 15 / 100
if salario > 1250.00:
    print('Seu salário ficou com um aumento de 10%, então você ganhará R${}'.format(salario + c))
else:
    print('Seu salário ficou com um aumento de 15%, então você ganhará R${}'.format(salario + q))