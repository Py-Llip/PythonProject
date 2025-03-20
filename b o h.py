'''#1257 octal
n1 = int(input(': '))
n2 = int(input(': '))
n3 = int(input(': '))
n4 = int(input(': '))
q = n1 * 8**4 + n2 * 8**2 + n3 * 8**1 + n4 * 8**0
print(q)
#Tansformar número octal tansformando a decimal î
# Hexadecimal
n11 = int(input(': '))
n21 = int(input(': '))
n31 = int(input(': '))
n41 = int(input(': '))
a = 10
b = 11
c = 12
d = 13
g = n11 * 16**3 + n21 * 16**2 + n31 * 16**1 + n41 * 16**0
print(g)'''
# transformar um número decimal em binário
na = int(input(': '))
#nb = int(input(': '))
#nc = int(input(': '))
#nd = int(input(': '))

r = na % 2
e1 = na // 2
k = e1 % 2
e2 = e1 // 2
j = e2 % 2
e3 = e2 // 2
l = e3 % 2
e4 = e3 // 2
u = e4 % 2
print(u, l, j, k, r)
# transformando numero hexadecimal em binário Î
