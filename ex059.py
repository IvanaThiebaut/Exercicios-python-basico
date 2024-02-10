num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''--- O que deseja fazer? ---
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Qual sua opção?  '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'. format(num1, num2, soma))
    elif opcao == 2:
        multi = num1 * num2
        print('A multiplicação de {} por {} é {}'.format(num1, num2, multi))
    elif opcao == 3:
        if num1 > num2:
            print('O numero {} é maior que {}.'.format(num2, num1))
        elif num1 == num2:
            print('Os numeros sao iguais.')
        else:
            print('O numero {} é maior que {}.'.format(num1, num2))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        num1 = int(input('primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('finalizando..')
    else:
        print('Opcao invalida. Tente novamente')
print('Fim do programa! volte sempre')
