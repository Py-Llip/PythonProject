from time import sleep
num = int(input('Digite um número de 0-9999: '))
print('\033[4;97;40mPROCESSANDO...\033[m')
#sleep(3)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[1;35;46mUnidade: {} \033[m'.format(u))
print('\033[1;31;46mDezena: {:^3}\033[m'.format(d))
print('\033[1;33;46mCentena: {} \033[m'.format(c))
print('\033[1;32;46mMilhar :{:^3}\033[m'.format(m))
