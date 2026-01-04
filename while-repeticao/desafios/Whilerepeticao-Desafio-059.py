
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
maior = 0
opcao = 0
while opcao != 5:
    opcao = int(input('Digite um dos números a seguir para que a operação seja concluída:\n[1]Somar\n[2]Multiplicar\n[3]Maior valor\n[4]Novos números\n[5]Sair do programa\n: '))
    if opcao == 1:
        s = n1 + n2
        print(s)
    elif opcao == 2:
        m = n1 * n2
        print(m)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(maior)
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
print('Programa Finalizado.')