l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print('Pode formar triangulo')
    if l1 == l2 and l2 == l3:
        print('Será um triangulo equilatero')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Será um triangulo isosceles')
    elif l1 != l2 and l2 !=l3 and l1 != l3:
        print('Será um triangulo escaleno.')
else:
    print('Não pode formar triangulo')