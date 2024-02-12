import random
tentativas = 0
numpc = random.randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10. Será que você consegue adivinhar?')
palpite = int(input('Qual seu palpite: '))
acertou = False
while palpite != numpc:
    palpite = int(input('Você errou, tente novamente'))
    tentativas += 1
if palpite == numpc:
    acertou = True
    print('Parabens você acertou!')
print('O numero de tentativas foi {}'.format(tentativas))