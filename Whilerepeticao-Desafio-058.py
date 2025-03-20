from random import randint
from time import sleep
cont = 1
sleep(2)
print('''\033[35;1m                                        
 ,_,  
(.,.) 
(   ) 
-"-"-- ''')
print('\033[36mLusPointsStudios')
sleep(4)
print('\033[36;1m~'+'\033[36;1mm\033[34;1mw'*30+'~')
print('\033[32;1mGameAlen')
n = randint(0, 10)
#print(n)
sleep(2)
d = int(input('\033[97;1mEscolha um NÚMERO de 0 à 10 \033[36;1m⊂(◉‿◉)つ\033[97m: '))
print('\033[97;4mPROCESSANDO...\033[m')
sleep(2)
while n != d:
    d = int(input('\033[31;1mVocê ERROU, que peninha \033[30;1m(҂◡_◡)\033[97;1m tente NOVAMENTE: '))
    print('\033[97;4mPROCESSANDO...\033[m')
    sleep(2)
    cont += 1
print('Você \033[33;1mGANHOU\033[97m! com \033[36;1m{}\033[97;1m TENTATIVAS!!! (-(-\033[34;1mu\033[97;1m-(-\033[32;1m0\033[97;1m(-c(\033[33;1m*\033[97;1mO\033[33;1m*\033[97;1m)\033[32;1mv\033[97;1m-)-\033[31;1mQ\033[97;1m-)-\033[36;1m*\033[97;1m)\033[35;1mU\033[97;1m-)-)'.format(cont))