colocados = ('Corinthians - Campeão', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético Mineiro', 'Botafogo', 'Atlético Paranaense', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Vitória', 'Coritiba - Rebaixado', 'Avaí - Rebaixado', 'Ponte Preta - Rebaixada', 'Atlético Goianiense - Rebaixado')
print(f'Os 5 primeiros colocados são: ')
for c in range(1,6):
    print(f'{colocados[c]} {c}°', end='')
    if c < 5:
        print(', ', end='')
    else:
        print('.', end='')
print(f'\nOs últimos 4 colocados são: ')
for i in range(15, 20):
    print(f'{colocados[i]} {i+1}°', end='')
    if i < 19:
        print(', ', end='')
    else:
        print('.', end='')
print(f'\nListagem em ordem alfabética:\n{sorted(colocados)}')
print(f'Chapecoense está na posição: {colocados.index('Chapecoense')+1}°')


