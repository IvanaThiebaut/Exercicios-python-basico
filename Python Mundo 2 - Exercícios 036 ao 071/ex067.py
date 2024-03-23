while True:
    n = int(input('Digite um numero para ver sua tabuada: '))
    if n <= 0:
        break
    for tab in range(1, 11):
        print(f'{n} x {tab} = {n * tab}')
