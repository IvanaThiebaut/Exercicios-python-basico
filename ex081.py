lista = []
r = 'S'
cont = 0
while r == 'S':
    n = int(input('Digite um numero: '))
    lista.append(n)
    cont += 1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
print(f'Foram digitados {cont} valores.')
lista.sort(reverse=True)
print(f'A lista dos valores em ordem decrescente é {lista}.')
if 5 in lista:
    print('O numero 5 está na lista')
else:
    print('O numero 5 não está na lista.')