from time import sleep
enter = str(input('='*38+'\n\033[7;32;107mDê ENTER para começar o game!\033[m ~(0u0)~!\n'+'='*38))
print(r'''           __
           /'{>
       ____) (____
     //'--;   ;--'\\
    ///////\_/\\\\\\\
           m m  ''')
sleep(2)
print('Desenvolvido por: Fellipe Alves B.')
sleep(2)
print('Em estado de teste')
sleep(2)
print('Lutas Entre Satéletes')
sleep(2)
op = ['a) O início de uma jornada','b) A fatoração estelar','c) O fim dos satéletes']
for i in op:
    print(i)
    sleep(2)
l = str(input('Digite uma letra no tópico que gostaria: '))
