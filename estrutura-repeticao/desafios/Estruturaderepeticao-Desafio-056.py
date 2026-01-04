si = 0
conti = 0
maior = 0
nomevelho = ''
conts = 0
for c in range(1,5):
    print('='*40,'\n{} Pessoa'.format(c))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: '))
    si += idade
    conti += 1
    if c == 1 and sexo == 'masculino':
        maior = idade
        nomevelho = nome
    if sexo == 'masculino' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo == 'feminino' and idade <= 20:
        conts += 1
print('A média de idade do grupo é {}\nExistem {} mulheres com menos de 20 anos\nA idade do homem mais velho tem {} e se chama {}'.format(si/conti, conts, maior, nomevelho))