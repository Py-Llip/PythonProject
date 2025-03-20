import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
#num = ('1°', '2°', '3°', '4°')
nomes = [n1, n2, n3, n4]
#sq = random.sample(num, k=4)
random.shuffle(nomes)
print('Ordem dos alunos {}'.format(nomes))


'''for i, nomes in enumerate(s, start=1):
    print('{}. {}'.format(i, nomes))'''
