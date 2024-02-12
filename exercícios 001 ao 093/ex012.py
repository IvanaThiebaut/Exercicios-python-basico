preco = float(input('Digite o preço do produto: '))
novo = preco - (preco * 5 / 100)
print('O produto que custava {}, na promoção com desconto de 5% vai custar apenas {}'.format(preco, novo))
