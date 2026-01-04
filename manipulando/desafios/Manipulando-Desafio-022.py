n = str(input('Digete seu nome completo: '))
lma = n.upper()
lmi = n.lower()
l = len(n.replace(' ', ''))
q = len(n.split())
pn = n.split()[0]
nlp = len(pn)
print('\033[33mO seu nome com letras maiúsculas é {},\n\033[34mO seu nome com letras minúsculas é {},\n\033[35mO números de letras do seu nome é {}\n\033[37me de letras do seu primeiros nome é {}'.format(lma, lmi, l, nlp))


