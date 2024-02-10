dist = float(input('Qual é a distância da viagem? '))
if dist < 200:
    v1 = dist * 0.5
    print('O valor da passagem será R$ {}.'.format(v1))
else:
    v2 = dist * 0.45
    print('O valor da passagem será {}.'.format(v2))
