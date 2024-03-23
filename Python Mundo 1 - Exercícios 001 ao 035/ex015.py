kms = float(input('Quantos kilometros você percorreu? '))
days = float(input('Quantos dias você ficou com o carro? '))
preco_dia = (days * 60)
preco_kms = (kms * 0.15)
total_aluguel = preco_dia + preco_kms
print('O valor que você deverápagar pela locaçãodo veiculo é de R${}.'.format(total_aluguel))