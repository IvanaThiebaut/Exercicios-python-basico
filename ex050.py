s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma dos numeros {} pares será {}.'.format(cont,s))