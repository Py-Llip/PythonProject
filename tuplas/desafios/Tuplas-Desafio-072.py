n = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    continuar = ''
    d = int(input('Digite um número entre 0 e 20: '))
    if 0 <= d <= 20:
        print(n[d])
        continuar = str(input('Deseja continuar? [S,N]')).strip().upper()[0]
        if continuar == 'S':
            print('Continuando...')
        else:
            break
    else:
        print('tente novamente')




