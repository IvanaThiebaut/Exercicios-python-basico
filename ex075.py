n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor {n2} apareceu na segunda posição.')
par = impar = 0
for n in numeros:
    if n !=0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Foram digitados {par} numeros pares')