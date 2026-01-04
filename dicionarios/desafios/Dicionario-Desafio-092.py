from datetime import datetime
dic = dict()
dic['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano
dic['idade'] = idade
dic['ctps'] = int(input('Carteira de Trabalho [Digite 0 se não tem]: '))
if dic['ctps'] != 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salário'] = float(input('Salário: R$'))
    dic['aposentadoria'] = dic['idade'] + ((dic['contratação'] + 35) - datetime.now().year)
print('-'*30)
print(dic)
print('-'*30)
for k, v in dic.items():
    print(f'{k} tem o valor {v}')