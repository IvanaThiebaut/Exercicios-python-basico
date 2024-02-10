n = str(input('Digite o seu nome completo: ')).strip()
nomes = n.split()
print('O primeiro nome da pessoa é {} e o ultimo nome é {}.'.format(nomes[0],nomes[-1]))