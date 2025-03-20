dic = dict()
dic['Nome'] = str(input('Nome: '))
dic['Idade'] = float(input(f'Média de {dic['Nome']}: '))
if dic['Idade'] <= 7:
    dic['Situação'] = 'Reprovado'
else:
    dic['Situação'] = 'Aprovado'
for k, v in dic.items():
    print(f'{k} é igual a {v}')

