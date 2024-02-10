temp = []
princ = []
leves = []
pesadas = []
r = 'S'
cont = 0
while r == 'S':
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    princ.append(temp[:])
    temp.clear()
    cont += 1
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
print(f'Foram adicionadas {cont} pessoas')
for p in princ:
    if p[1] <= 50:
        leves.append(p[0])
    else:
        pesadas.append(p[0])
print(f'Lista das pessoas mais pesadas: {pesadas}')
print(f'Lista das pessoas mais leves: {leves}')