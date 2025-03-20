
v = float(input('Quantos Km vicê irá viajar? '))
cobranca1 = v * 0.50
cobranca2 = v * 0.45
if v <= 200.0:
    print('Seus Km que irá percorrer sendo {}Km, é menor que 200Km'.format(v))
    print('Então você  irá pagar R$0.50 por cada Km, que será de R${:.2f}'.format(cobranca1))
else:
    print('Seus Km que irá percorrer sendo {}Km, é maior que 200Km'.format(v))
    print('Então você irá pagar R$0.45 por cada Km, que será de R${:.2f}'.format(cobranca2))
