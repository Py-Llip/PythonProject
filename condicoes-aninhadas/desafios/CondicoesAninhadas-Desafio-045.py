from random import randint
frase = str(input('Escreva Pedra, Papel, ou Tesoura: '))
frase1 = frase.upper()
if frase1 == 'PEDRA':
    print('a')
elif frase1 == 'PAPEL':
    print('b')
elif frase1 == 'TESOURA':
    print('c')
else:
    print('Não existe {}'.format(frase))
computador = randint(1, 3)
#PEDRA
if computador == 1 and frase1 == 'PEDRA':
    print('Eu escolhi PEDRA e você também escolheu, Empate')
elif computador == 2 and frase1 == 'PEDRA':
    print('Eu escolhi PAPEL então você PERDEU, boa sorte da próxima vez')
elif computador == 3 and frase1 == 'PEDRA':
    print('Eu escolhi TESOURA então você GANHOU!!!, boa d+')
#PAPEL
if computador == 1 and frase1 == 'PAPEL':
    print('Eu escolhi PEDRA então você GANHOU!!!, boa d+')
elif computador == 2 and frase1 == 'PAPEL':
    print('Eu escolhi PAPEL e você também escolheu, Empate')
elif computador == 3 and frase1 == 'PAPEL':
    print('Eu escolhi TESOURA então você PERDEU, boa sorte da próxima vez')
#TESOURA
if computador == 1 and frase1 == 'TESOURA':
    print('Eu escolhi PEDRA então você PERDEU, boa sorte da próxima vez')
elif computador == 2 and frase1 == 'TESOURA':
    print('Eu escolhi PAPEL então você GANHOU!!!, boa d+')
elif computador == 3 and frase1 == 'TESOURA':
    print('Eu escolhi TESOURA e você também escolheu, Empate')


