n = float(input('Digite seu preço: '))
r = 5 / 100 * n
m = n - r
print('Esta promoção indica que você tem 5% de desconto, que seu valor vai ficar com R${:.3f}'.format(m))
