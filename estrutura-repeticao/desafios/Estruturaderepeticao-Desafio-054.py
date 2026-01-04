cont = 0
twocont = 0
idades = []
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = 2024 - ano
    idades.append(idade)
    if ano >= 18:
        cont += 1
    else:
        twocont += 1
for idade in idades:
    if idade >= 18:
        print('\033[31m{}-, '.format(idade), end='')
    else:
        print('\033[34m{}, '.format(idade), end='')

print('\n\033[mDentre essas idades são maiores \033[31m{}\033[m e menores \033[34m{}'.format(cont, twocont))
