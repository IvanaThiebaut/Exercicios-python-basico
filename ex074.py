import random
num = (random.randint(0, 100), random.randint(0, 100),random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
print(f'Eu sorteei os valores ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
