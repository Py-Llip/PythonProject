f = str(input('Sua palavra é um Pal[indromo? ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')

