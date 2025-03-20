'''nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))'''


n1 = float(input('Digite: '))
n2 = float(input('Digite outro: '))
n = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(n))
if n >= 6.0:
    print('Boa nota!')
else:
    print('Vai estudar seu burro!')

