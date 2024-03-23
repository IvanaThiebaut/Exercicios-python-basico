n = int(input('Digite um numero para ver sua tabuada: '))
for tab in range(0, 10):
    print('{} x{:2} = {}'.format(n, tab + 1, n * (tab + 1)))