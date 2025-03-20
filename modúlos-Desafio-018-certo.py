from math import radians, sin, cos, tan
from fractions import Fraction
a = float(input('Digite um angulo qualquer: '))
ar = radians(a)
sen = (sin(ar))
cos = (cos(ar))
tg = (tan(ar))

print('O angulo do seno é \033[32m{:.2f}\033[34m°\033[m'.format(sen))
print('O angulo do cosseno é \033[32m{:.2f}\033[34m°\033[m'.format(cos))
print('O angulo do tangente é \033[32m{:.2f}\033[34m°\033[m'.format(tg))
