preco = float(input('Qual o preço do produto? ' ))
print('O preço do produto é {}. Como você deseja realizar o pagamento?'.format(preco))
print('Selecione a forma de pagamento:')
print('''[1] A vista dinheiro/cheque
[2] A vista no cartão
[3] em até 3x no cartão
[4] em 3x ou mais no cartão''')
opcao = int(input('Forma de pagamento: '))
if opcao == 1:
    print('Você recebeu um desconto de 10%, o valor a ser pago pelo produto será de R${}.'.format(preco - (preco * 0.1)))
elif opcao == 2:
    print('Você recebeu um desconto de 5%, o valor a ser pago pelo produto será de R${}.'.format(preco - (preco * 0.05)))
elif opcao == 3:
    print('Você deverá pagar R${} pelo produto.'.format(preco))
elif opcao == 4:
    print('Optanto por essa forma de pagamento você pagará um juros de 20%, o valor a ser pago pelo produto será de R${}.'.format(preco + (preco * 0.2)))
