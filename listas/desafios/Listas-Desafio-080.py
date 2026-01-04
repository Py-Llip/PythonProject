lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or lista[-1] <= n:
        lista.append(n)
        print(f'O valor {n} foi adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O valor {n} foi adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista)

