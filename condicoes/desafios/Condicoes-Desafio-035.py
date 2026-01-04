r1 = float(input('Digite um comprimento da primeira reta: '))
r2 = float(input('Digite um comprimento da segunda reta: '))
r3 = float(input('Digite um comprimento da terceira reta: '))
#q1 = r1 + r2 > r3
#print(q1)
#q2 = r1 + r3 > r2
#print(q2)
#q3 = r2 + r3 > r1
#print(q3)
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Esses segmentos podem se juntar para formar um triangulo! :)')
else:
    print('Esses segmentos não podem se juntar para formar um triangulo :(')
