from random import randint
eu = partidas = soma = 0
par = 'P'
impar = 'I'
print('-' * 6, 'VAMOS JOGAR PAR OU IMPAR', '-' * 6)
while True:
    eu = int(input('Diga um valor: '))
    pc = randint(0, 10)
    escolha = input('Par ou impar? [P/I] ').strip().upper()
    while escolha not in 'PI':
        escolha = input('Par ou impar? [P/I] ').strip().upper()
    soma = pc + eu
    partidas += 1
    if escolha == 'I':
        if soma %2 != 0:
            print(f'Voce escolheu {eu} e o computador escolheu {pc}, a soma deu {soma}, e é IMPAR, voce GANHOU!')
        if soma % 2 == 0:
            print(f'Voce escolheu {eu} e o computador escolheu {pc}, a soma deu {soma}, e é PAR, voce PERDEU :(')
            break
    if escolha == 'P':
        if soma % 2 != 0:
            print(f'Voce escolheu {eu} e o computador escolheu {pc}, a soma deu {soma}, e é IMPAR, voce PERDEU :(')
            break
        if soma % 2 == 0:
            print(f'Voce escolheu {eu} e o computador escolheu {pc}, a soma deu {soma}, e é PAR, voce GANHOU!')
print(f'Você jogou {partidas} partidas antes de perder.')