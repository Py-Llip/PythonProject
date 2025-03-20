'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutaveis
#lanche[1] = 'Refrigerante' este comando está errado
#print(lanche)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi tudo')
print(len(lanche))
for cont in range(0, len(lanche)):
    print(lanche[cont], cont)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) organiza as tuplas em ordem alphabetica
print(lanche)
a = (2, 5, 4)
b = (5,8,1,2)
c = a + b
#print(c.count(4)) quantas vezes aparece
print(c.index(8, 1))#em que  posicao esta o 8 e o '1' serve pra iniciar em uma posicao'''
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)#apaga a variavel
print(pessoa)



n = (0,1,2,3,'F')
for c in n:
    print(c, end='')
print('FIM')
#for cont in range(0, len(n)):
#    print(n[cont])
for e, t in enumerate(n):
    print(t, e)
