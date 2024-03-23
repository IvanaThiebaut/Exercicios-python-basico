casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salário mensal? '))
anos = float(input('Em quantos anos você pretende pagar a casa?' ))
prest = casa/(anos * 12)
if prest <= sal/3:
    print('Parabens, seu emprestimo foi concedido')
else:
    print('Seu imprestimo foi negado.')
print('A parcela seria de {}.'.format(prest))