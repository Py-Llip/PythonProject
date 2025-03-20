dic = dict()
lis = list()
todopart = list()
while True:
    total = 0
    todopart.clear()
    dic["nome"] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    for p in range(0, partidas):
        ng = int(input(f'Quantos gols na partida {p}?'))
        todopart.append(ng)
        total += ng
    dic["gols"] = todopart.copy()
    dic["total"] = total
    seguir = ''
    while seguir not in ['S', 'N']:
        seguir = str(input('Deseja continuar? [S, N]')).upper()[0]
        if seguir not in ['S', 'N']:
            print('ERRO!, tente novamente.')
    lis.append(dic.copy())
    if seguir in 'N':
        break
print('=-'*30)
print(lis)
print('-'*50)
print(f'{"TABELA":_^50}')
print('-'*50)
print(f'{"N°":<4}{"NOME":<19}{"GOLS":<22}{"TOTAL":>5}')
print('-'*50)
for n, t in enumerate(lis):
    print(f'{n:<4}{t["nome"]:<19}{str(t["gols"]):<22}{t["total"]:>5}')
print('-'*50)
while True:
    dados = int(input('Deseja mostar dados de qual jogador[999>Finaliza]? [N°]'))
    if dados == 999:
        break
    elif dados >= len(lis) or dados < 0:
        print('ERRO!')
    else:
        print(f'DADOS DO JOGADOR {lis[dados]["nome"]}:')
        for n, c in enumerate(lis[dados]["gols"]):
            print(f'No jogo {n} fez {c} gols')

print('Programa Finalizado')






