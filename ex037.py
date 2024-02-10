num = int(input('Escreva um numero inteiro: '))
print('Qual base de conversão? ')
print('''[A] - Coverter para binario
[B] - Converter para Octal
[C] - Converter para Hexadecimal''')
escolha = input('Qual será a base escolhida? ').upper()
if escolha == 'A':
    print('O {} convertido para binário é {}'.format(num, bin(num)[2:]))
elif escolha == 'B':
    print('O {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 'C':
    print('O {} convertido em Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
