print('-' * 20)
print('    LOJA DA IVANA    ')
print('-' * 20)
prod = ''
barato = ''
preco = totalcompra = prodcaros = 0
menor = cont = 0
r = 'S'
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    if cont ==1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = prod
    totalcompra += preco
    if preco >= 1000:
        prodcaros += 1
    r = input('Quer continuar? [s/n] ').strip().upper()[0]
    while r not in 'SN':
        r = input('Quer continuar? [s/n] ').strip().upper()[0]
    if r == 'N':
        break
print('----FIM DO PROGRAMA----')
print(f'O total da compra foi R${totalcompra}')
print(f'Temos {prodcaros} produtos custando mais de R$1000.')
print(f'O produto mais barato foi {barato}')
