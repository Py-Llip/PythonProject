def notas(*num, sit=False):
    """=>Função a calcular diversas atividades de números sobre notas em um dicionário:
        :parametro *num: Coloque quaisquer números para cálculos de atividades disponíveis.
        :parametro sit: Quando ativada, mostra a situação em relação a média.
        :returm: dicionário que mostra os dados feitos."""
    dic = dict()
    dic["total"] = len(num)
    maior = menor = 0
    soma = 0
    for e, v in enumerate(num):
        if e == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
        soma += v
    dic["maior"] = maior
    dic["menor"] = menor
    media = soma / len(num)
    dic["media"] = f'{media:.2f}'
    if sit:
        if float(dic["media"]) < 5:
            dic["situação"] = 'RUIM'
        elif 5 < float(dic["media"]) < 7:
            dic["situação"] = 'Razoável'
        else:
            dic["situação"] = 'BOM'
    return dic
resp = notas(3.5, 5, 6.5, 10, 7, 4, sit=True)
print(resp)
help(notas)