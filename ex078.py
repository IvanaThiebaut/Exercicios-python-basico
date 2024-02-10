valores = []
menor = maior = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digit um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('-=' * 10)
print(valores)
print(f'O menor valor digitado foi {maior} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O maior valor digitado foi {menor} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
