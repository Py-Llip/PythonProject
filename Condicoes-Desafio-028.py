import random
import time
n = random.randint(0, 5)
print('\033[31m-\033[32m=\033[36m-\033[m' * 11)
s = int(input('Tente adivinhar um número de \033[34m0\033[m a \033[32m5\033[m: '))
print('\033[31m-\033[32m=\033[36m-\033[m' * 11)
print('\033[4;97;40mPROCESSANDO...\033[m \033[31m(\033[32m~\033[36mO\033[31m-\033[32mO\033[36m)\033[31m~\033[m')
time.sleep(3)
if s == n:
    print('\033[33m*\033[32mVocê acertou !(~0-0)~ {}\033[33m*\033[m'.format(n))
else:
    print('\033[33m!\033[31mVocê errou :( o número era {}\033[33m!\033[m'.format(n))
