import random
escolha = str(input('Você escolhe pedra, papel ou tesoura? ')).upper()
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.choice(opcoes)
print('O computador escolheu {}.'.format(pc))
if escolha == pc:
    print('O jogo deu empate.')
elif escolha == 'PAPEL' and pc == 'PEDRA':
    print('papel vence pedra, você venceu')
elif escolha == 'PAPEL' and pc == 'TESOURA':
    print('Tesoura ganha de papel, você perdeu.')
elif escolha == 'PEDRA' and pc == 'PAPEL':
    print('Papel vence pedra, você perdeu.')
elif escolha == 'PEDRA' and pc == 'TESOURA':
    print('Pedra ganha de tesoura, você ganhou.')
elif escolha == 'TESOURA' and pc == 'PAPEL':
    print('Tesoura ganha de papel, você ganhou.')
elif escolha == 'TESOURA' and pc == 'PEDRA':
    print('Pedra ganha de tesoura, você perdeu.')