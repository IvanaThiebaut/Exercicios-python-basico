n = int(input('Quantos termos você quer mostrar: '))
ultimo = 1
penultimo = 1
if (n == 1) or (n == 2):
    print('1')
else:
    conta = 3
    while conta <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        conta += 1
        print(termo)