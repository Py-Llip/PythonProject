import math
import time
v = float(input('Por favor, coloque a velocidade do seu carro Km/h: '))
multa = (v - 80.0) * 7.00
if v > 80.0:
    print('\033[31mVocê foi multado!\033[m')
    time.sleep(2)
    print('\033[1;33mA multa vai custar R$7.0 por cada Km acima do limite\033[m')
    time.sleep(2)
    print('A multa vai custar \033[32mR$\033[1;30;42m{}\033[m'.format(multa))
    time.sleep(2)
else:
    print('Pode ir em paz...')
print('Tenha um bom dia')
