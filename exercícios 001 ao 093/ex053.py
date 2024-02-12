frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('temos um palindromo!')
else:
    print(' a frase nao é palindromo')
print('Você digitou a frase {}.'. format(frase))
