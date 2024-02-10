lista = []
pares = []
impares = []
r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=' * 10)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

