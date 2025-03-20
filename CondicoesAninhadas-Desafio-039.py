from datetime import datetime
anoatual = datetime.now().year
anonascimento = int(input('Coloque seu ano de nascimento: '))
#2006 = 18
c = anoatual - anonascimento
if c < 18:
    print('Você não tem idade o suficuente para se alistar com {} anos\nVocê precisa de mais {} anos pra se alistar.'.format(c, 18 - c))
elif c == 18:
    print('É hora de você, meu pequeno gafanhoto, se alistar! Pois completou 18 anos!')
else:
    print('já passou {} anos para o seu alistamento'.format(c - 18))
