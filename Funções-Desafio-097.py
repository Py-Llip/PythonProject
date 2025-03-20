def escreva(msg):
    deco = len(msg) + 2
    print('-' * deco)
    print(f'{msg:^{deco}}')
    print('-' * deco)

escreva('Olá, Mundo!')
escreva('Fellipe')
escreva('O pato Morreu Morrido na pata da garça namorada da amada e dramatica')