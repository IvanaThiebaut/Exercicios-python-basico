matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz [l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-' * 30)
print(f'A soma dos valores pares é {somapar}')
for l in range (0, 3):
    somacoluna += matriz [l][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')
for c in range(0, 4):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][2] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
