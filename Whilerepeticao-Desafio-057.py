s = str(input('Digite [M] sendo masculino e [F] feminino de acordo com seu sexo: [M,F]')).strip().upper()[0]
while s not in 'MF':
#while s != 'MASCULINO' and s != 'FEMININO':
    s = str(input('Dados inválidos, please informe seu sexo: ')).strip().upper()[0]

print('FIM')
