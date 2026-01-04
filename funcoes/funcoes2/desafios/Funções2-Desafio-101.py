
# mais de 65 voto opcional tambén cin 16 e menos n vota
def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    print('-'*30)
    if 65 > idade >= 18:
        return f'VOTO OBRIGATÓRIO'
    elif 18 > idade >= 16 or idade >= 65:
        return f'VOTO OPCIONAL'
    else:
        return f'NÃO VOTA'


print(voto(int(input('Digite seu ano de nascimento: '))))
