'''*Interactive Help*
Para obter essa função interna é preciso usar o help()
serve para ajudar, exemplo: help(print) = faz uma explicação, é possível fazer também no console do python se preciso

*Docstrings*
Ela serve para explicar um comando que o help não consegue explicar(VocÊ CRIA seu help)
ex """-> Faz uma coisa este comando"""

*Parâmetros Opcionais*
Faz um parametro opcional ex:
def somar(a,b,c=0):...
somar(8,4)
Não existe o c então podemos colocar o '=0'

*Escopo de Variáveis*
O local onde a variável vai existe e o local de onde não vai existir (variavel local dentro do dev e a variavel global fora e dentro) em funções

*Retorno de Valores*
Retornar o valor ou não nas funções(return)
ex
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3,6,1)
r2 = somar(5,1)
r3 = somar(8)
print(r1, r2, r3)'''

