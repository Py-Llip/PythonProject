

print('CADASTRE UMA PESSOA')
sexo = continuar = ''
contsm = contsf = conti = 0

while True:
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        conti += 1
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite seu sexo [M,F]: ')).strip().upper()[0]
        if sexo == 'M':
            contsm += 1
        elif sexo == 'F' and idade < 20:
            contsf += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar a cadastrar mais pessoas? [S,N]: ')).strip().upper()[0]
        while continuar != 'S' and continuar != '' and continuar != 'N':
            print('Dado inválido, tente novamente')
            continuar = ''
    if continuar == 'N':
        break
    sexo = continuar = ''
print(f'Pessoas com 18 ou mais {conti}\n{contsm} Homens cadastrados\nE temos {contsf} mulheres com menos de 20 anos')

