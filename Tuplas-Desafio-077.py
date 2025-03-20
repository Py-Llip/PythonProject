palavra = ('Papel', 'Mesa','Paralelepipedo')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in range(0, len(palavra)):
    print(f'\nA palavra: {palavra[c]} tem ', end='')
    for i in range(0, len(palavra[c])):
        for x in range(0, len(vogais)):
            if vogais[x] == palavra[c][i]:
                print(f'"{vogais[x]}" ', end='')
    print('de vogais')
