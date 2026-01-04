lista = []
while True:
    nomel = []
    notal = []
    nome = str(input('Nome: '))
    nomel.append(nome)
    for n in range(0,2):
        nota = float(input(f'Nota {n+1}: '))
        notal.append(nota)
    nomel.append(notal[:])
    lista.append(nomel[:])
    nomel.clear()
    notal.clear()
    seguir = ''
    while seguir not in ['S','N']:
        seguir = str(input('Continuar [S,N]: ')).strip().upper()[0]
        if seguir not in ['S', 'N']:
            print('Dado inválido, tente novamente:')
    if seguir in 'N':
        break
medial = []
for m in range(0, len(lista)):
    media = (lista[m][1][0] + lista[m][1][1]) / 2
    medial.append(media)
    lista[m].append(medial[m])
#Boletim
print('-'*30)
print(f'{'BOLETIM':^30}')
print('-'*30)
print(f'{"Nº":<4}{"NOME":<15}{"MÉDIA":>10}')
for b in range(0, len(lista)):
    print(f'{b:<4}{lista[b][0]:<15}{lista[b][2]:>10}')
print('-'*30)
continuar = -1
while continuar != 999:
    continuar = int(input('Mostar quais notas de qual aluno? [999 interrompe]: '))
    if continuar != 999:
        print(f'Notas de {lista[continuar][0]} são {lista[continuar][1]}')
print('FINALIZANDO...')