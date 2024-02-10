velo = float(input('Qual a velocidade atual do carro? '))
multa = (velo - 80) * 7
if velo <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Sua velocidade está acima do permitido, sua multa vai custar {}!'.format(multa))
