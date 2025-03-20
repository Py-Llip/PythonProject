'''pessoas = {'nome': 'Fellipe',
           'sexo': 'M',
           'idade': 15}
del pessoas['sexo']
pessoas['nome'] = 'Gustavo'
pessoas['peso'] = 98.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(k, v)
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1, brasil)
print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(k, v)
