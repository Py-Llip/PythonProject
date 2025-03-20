from random import randint
menor = maior = 0

for c in range(0,5):
    s = (randint(0, 9))
    if c == 0:
        maior = s
        menor = s
    elif maior < s:
        maior = s
    elif menor > s:
        menor = s
    print(f'{s} ', end='')
print(f'maior {maior}, menor {menor}')


