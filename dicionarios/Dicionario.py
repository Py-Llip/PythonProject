#Dicionarios são indentificados com {}
#dados = dict()
#dados = {'nome':'Pedro', 'idade':25}
#print(dados['nome']) == 'Pedro'
#dados['sexo'] = 'M' == {'nome':'Pedro', 'idade':25, 'sexo':'M'}
#del dados['idade'] == {'nome':'Pedro', 'sexo':'M'}

#filme = {'titulo':'Star Wars',
# 'ano':1997,
# 'diretor':'George Lucas'
#}
#print(filme.values()) isso retorna todos os valores do filme == Star Wars, 1997, George Lucas
#print(filme.keys()) isso retorna as chaves == titulo, ano, diretor
#print(filme.items()) pega todos
#for k, v in filme.items():
#   print(f'O {k} é {v})

#filme = {'titulo':'Star Wars', 'ano':1997}
#chave = list(filme.keys())
#valor = list(filme.values())
#for c in range(0, len(filme)):
#    print(f'O valor {valor[c]} está na chave {chave[c]}')
#print(filme)

#pode juntar lista com dicionarios e tuplas ex:
#locadora = list([filme])
#print(locadora[0]['ano'])
