temp = []
princ = []
impares = []
pares = []
for c in range (0, 7):
    temp.append(int(input(f'Digite o {c + 1}° valor: ')))
    princ.append(temp[:])
    temp.clear()
for p in princ:
    if p[0] % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
pares.sort()
impares.sort()
print('-' * 20)
print(f'Os valores digitados foram: {princ}')
print(f'Os valores pares são: {pares}')
print(f'Os valores impares são: {impares}')
