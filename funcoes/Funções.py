'''função é uma maneira de simplicar o código em python
ex
def mostraLinha():
    print('repeticao')
ele n executa o def
ele excutaa apenas o
mostraLinha()
ex
def lin():
    print('-'*30)


lin()
print('-'*30)
print('Felipão')
print('-'*30)
lin()

há parametros para personalisar ainda mais
ex
def mensagem(msg):
    print('-------')
    print(msg)
mensagem('SISTEMA DE ALUNOS')
a frase sistema de - se transforma em msg
ex
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-' * 30)


titulo('Feijão')
titulo('Felipão')
titulo('Açucar')

tem como empacotar parametros
ex
def contador(*núm):

contador(5,3,5,3,5,3)
contador(6,67,4)

da pra mecher com listas
ex
def dobra(lst):
    pos = 0
    while pos < len(lst):
    lst[pos]*= 2
    pos += 1


valores[1,2,3]
dobra(valores)
'''

