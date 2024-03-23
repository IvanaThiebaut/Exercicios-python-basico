from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('-' * 30)
print('Valores sorteados:')
print('-' * 30)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print()
print('RANKING DO JOGO')
ranking = sorted(jogo.items(),key=itemgetter(1))
ranking.sort(reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

