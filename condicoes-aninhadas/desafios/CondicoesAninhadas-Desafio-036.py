print('Bom dia!')
print('\033[32m-=-\033[m' * 7)
print('\033[34mEmpréstimo bancário:')
print('\033[32m-=-\033[m' * 7)
valordacasa = float(input('Por favor, coloque o Valor da casa: R$'))
salario = float(input('Por favor novamente, coloque o seu Salário: R$'))
anos = int(input('Por favor pela ultima vez, Quantos anos irá ser? '))
prestacao = valordacasa / (anos * 12)
minimo = salario * 30 / 100
#q = salario * 30 / 100
if prestacao <= minimo:
    print('Empréstimo ACEITO \033[32m!OuO!\033[m')
else:
    print('Empréstimo NEGADO \033[31m!ò~ó!')

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valordacasa, anos, prestacao))
