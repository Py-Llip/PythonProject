valor = float(input('Digite o valor do produto: '))
print('À vista \033[34mdinheiro/cheque\033[m (\033[31m1\033[m)\n10% de desconto')
print('À vista no \033[34mcartão\033[m (\033[31m2\033[m)\n5% de desconto')
print('Em até \033[34m2x no cartão\033[m (\033[31m3\033[m)\npreço normal')
print('\033[34m3x ou mais\033[m no cartão (\033[31m4\033[m)\n20% de juros')
cond = str(input('Digite o número da sua escolha: '))
if cond == '1':
    print('À vista ficará \033[34mdinheiro/cheque \033[32mR$ \033[42;30;1m{:.2f}\033[m'.format(valor - (valor * 10/100)))
elif cond == '2':
    print('À vista no \033[34mcartão\033[m \033[32mR$ \033[42;30;1m{:.2f}\033[m'.format(valor - (valor * 5/100)))
elif cond == '3':
    print('Em até 2x \033[34mno cartão \033[32mR$ \033[42;30;1m{:.2f}\033[m'.format(valor))

elif cond == '4':
    print('\033[34m3x ou mais \033[32mR$ \033[42;30;1m{:.2f}\033[m'.format(valor + (valor * 20/100)))
else:
    print('O número \033[31m{}\033[m é inexistente'.format(cond))
