def fatorial(num, show=False):
    """===>Uma ferramenta Maginifica para fatorações simples,
    :parâmetro n: coloque qualquer número inteiro para o resultado.
    :parâmetro show: sendo no segundo parâmetro uma configuração:
    dedica-se em mostrar apenas o resultado ou o caminho do resultado.
    Para ativa-la use 'show=True' e desativa-la 'show=False'.
    :return: O valor do fatorial de um número n."""

    fat = num
    f = 1
    while fat > 1:
        f *= fat
        fat -= 1
    if show:
        for c in range(num, 0, -1):
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' =', end=' ')

    return f
print(fatorial(5, show=True))
help(fatorial)