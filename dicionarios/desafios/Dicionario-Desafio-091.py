'''from random import randint
print('=-'*30)
dic = {}
lis = []
for a in range(0, 4):
    n = randint(1, 6)
    lis.append(n)
lis.sort()
dic['Num'] = lis
maior = 0
for k, c in dic.items():
    for l in range(0, len(dic["Num"])):
        if l == 0:
            maior = dic["Num"][l]
        elif maior < dic["Num"][l]:
            maior = dic["Num"][l]

print(f'Em todos os dados {dic.values()} o maior e Vencedor número foi {maior}')'''
from random import randint
from operator import itemgetter
from time import sleep
jogo = {'J1': randint(1, 6),
        'J2': randint(1, 6),
        'J3': randint(1, 6),
        'J4': randint(1, 6)}
print(f'Os valores sorteados foram:')
ranking = list()
for k, v in jogo.items():
    print(f'Jogador {k} tirou {v} no dado')
    sleep(0.2)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
