s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c
print('O somatorio dos {} numeros impares multiplos de 3 será {}'.format(cont,s))
