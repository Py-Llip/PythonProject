dic = dict()
lis = list()
dic["nome"] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for c in range(0, partidas):
    lis.append(int(input(f'Quantos gols na partida {c}?')))
dic["gols"] = lis.copy()
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {dic["nome"]} jogou {len(dic["gols"])} partidas.')
total = 0
for c in range(0, partidas):
    print(f'Na partida {c}, fez {dic["gols"][c]} gols')
    total += dic["gols"][c]
dic["total"] = total
print('=-'*30)
print(dic)
print('=-'*30)
print(f'Foi um total de {dic["total"]} gols')