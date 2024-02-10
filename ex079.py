valores = []
r = 'S'
while r == 'S':
    valores.append(int(input('Digite um valor: ')))
    if valores[-1] in valores[0:-1]:
        valores.pop()
        print('Valor duplicado, nao vou adicionar..')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
valores.sort()
print(valores)