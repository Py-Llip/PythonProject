nome = str(input('Qual é seu nome? '))
print('Tenha um bom dia {}' .format(nome))
if nome == 'Fellipe':
    print('Que nome mais bonitao {} \033[34m°O°\033[m'.format(nome))
elif nome == 'Bianca' or nome == 'Barbara' or nome == 'Bárbara':
    print('Que nome mais feio do mundo \033[31mò~ó\033[m')
else:
    print('Que nome normal O-O')

