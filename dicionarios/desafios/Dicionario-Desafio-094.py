lis = list()
dic = dict()
while True:
    dic.clear()
    continuar = ''
    dic["nome"] = str(input('Nome: '))
    dic["sexo"] = ''
    while dic["sexo"] not in ['M', 'F']:
        dic["sexo"] = str(input('Sexo: [M,F]')).upper()[0]
        if dic["sexo"] not in ['M', 'F']:
            print('Erro!, Responda apenas M(Masculino) ou F(Feminino).')
    dic["idade"] = int(input('Idade: '))
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S, N]')).upper()[0]
        if continuar not in ['S', 'N']:
            print('Erro!, Responda apenas S(Sim) ou N(Não).')
    lis.append(dic.copy())
    if continuar in ['N']:
        break
print('=-'*30)
print(lis)
print('=-'*30)
print(f'Temos cadastradas {len(lis)} pessoas.')
soma = 0
for c in range(0, len(lis)):
    soma += lis[c]["idade"]
media = soma / len(lis)
print(f'A média de idade é de {media:5.2f} anos.')
mulheres = list()
for c in range(0, len(lis)):
    if lis[c]["sexo"] == 'F':
        mulheres.append(lis[c]["nome"])
print(f'As mulheres cadastras são ', end='')
for c in range (0, len(mulheres)):
        print(f'{mulheres[c]}', end='')
        if mulheres[c] != mulheres[-1]:
            print(', ', end='')
        else:
            print('.', end='')
print(f'\nLista das pessoas que estão acima da média:')
for c in lis:
    if c["idade"] >= media:
        for k, v in c.items():
            print(f'{k} = {v}', end=' ')
print('Terminado')