def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


nom = str(input('Nome do jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nom.strip() == '':
    print(ficha(gols=gol))
else:
    print(ficha(nom, gol))

