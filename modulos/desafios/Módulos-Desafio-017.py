import math
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
r = math.pow(co, 2) + math.pow(ca, 2)
m = math.sqrt(r)
print('Então a Hipotenusa do seu triangulo retangulo é {:.3f}'.format(m))
# r = math.hypot(co, ca)
