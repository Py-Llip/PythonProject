print('-'*39)
titulo = 'LISTAGEM DE PREÇOS'
print(f'{titulo:^38}')
print('-'*39)
arm = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0, len(arm), 2):
    k = arm[c]
    x = len(arm[c])
    preco = arm[c+1]
    print(k+'.'*(30-x)+'R$',f'{preco:>6.2f}')

