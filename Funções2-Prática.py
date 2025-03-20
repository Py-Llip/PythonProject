
def fatorial(num=1):
    fat = num
    resp = 1
    while fat > 1:
        resp *= fat
        fat -= 1
    return resp

n1 = fatorial(3)
n2 = fatorial(4)
n3 = fatorial()
print(n1,n2,n3)


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite: '))
if par(num):
    print(par(num))
    print('É par')
else:
    print('Não é par')