def leiaint(msg):
    while True:
        valor = 0
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            return valor
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido:\033[m')


n = leiaint('Digite um número: ')
print(f'Você digitou o número inteiro {n}')