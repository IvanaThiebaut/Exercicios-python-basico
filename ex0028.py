from random import randint
computador = randint(0,5)
print('Eu pensei em um número de 1 a 5, você consegue descobrir?')
jogador = int(input('Diga qual numero você acha que eu pensei? '))
if jogador == computador:
    print('acertou miseravi, eu escolhi o numero {}!'.format(computador))
else:
    print('Não foi dessa vez, o numéro que eu escolhi foi {} e não o {}'. format(computador, jogador))