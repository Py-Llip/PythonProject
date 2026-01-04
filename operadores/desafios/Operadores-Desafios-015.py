qkm = float(input('Quantos km você percorreu? '))
qda = int(input('Quantos dias você alugou? '))
pd = 60 * qda
pk = 0.15 * qkm
print('A quantidade de km rodados no carro foi de {} km, se cada km custa R$ 0,15 você terá que pagar R$ {:.1f}\n E a quantidade de dias que você alugou foi {:.0f}, se cada dia custa R$ 60 você terá que pagar R$ {:.0f}'.format(qkm, pk, qda, pd))
