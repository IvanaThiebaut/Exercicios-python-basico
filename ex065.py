media = n = soma = cont = 0
r = 'S'
menor = maior = 0
while r == 'S':
    n = float(input('Digiete um numero: '))
    r = str(input('Quer continuar [s/n]: ')).strip().upper()[0]
    soma += n
    cont += 1
    media = soma / cont
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} numeros, a media foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
