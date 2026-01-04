'''teste = list()
teste.append('Fellipe')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste, galera)'''
#galera = [['ac3', 2], ['b', 1]]
#print(galera[0][0][2])

#for p in range(0, len(galera)):
#    print(f'{galera[p][0]} tem {galera[p][1]} anos de idade')
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
#print(galera, dado)
totmai = 0
totmen = 0
listm = []
listn = []
for p in galera:
    if p[1] >= 21:
        print(f'O {p[0]} é maior de idade')
        totmai += 1
        listm.append([p[0], p[1]])
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
        listn.append([p[0], p[1]])
print(f'Temos {totmai}, {listm} maior(es) de idade(s) e {totmen} {listn} menor(es) de idade(s)')
