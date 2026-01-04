from datetime import datetime
anonascimento = int(input('Coloque seu ano de nascimento: '))
anoatual = datetime.now().year
c = anoatual - anonascimento
if c <= 9:
    print('MIRIM')
elif c <= 14:
    print('INFANTIL')
elif c <= 19:
    print('JUNIOR')
elif c <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
print(c, 'anos')
