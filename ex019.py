import random
nome1 = str(input('Digite o primeiro aluno: '))
nome2 = str(input('Digite o segundo aluno: '))
nome3 = str(input('Digite o terceiro aluno: '))
nome4 = str(input('Digite o quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
