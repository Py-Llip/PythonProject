import math
from fractions import Fraction
a = float(input('Digite um angulo qualquer: '))
b = a * math.pi
w = Fraction(round(b), 180)
#ma = math.pi * a / 180

#    30°              | 45°              | 60°
#sen 1/2              | math.sqrt(2/2, 2)| math.sqrt(3/2, 2)
#cos math.sqrt(3/2, 2)| math.sqrt(2/2, 2)| 1/2
#tg  math.sqrt(3/3, 2)| 1                | math.sqrt(3, 2)
if 0 <= w <= 30:
    print('Sim')
else:
    print('Não')
#sen =
#cos =
#tg =

#print(w)
