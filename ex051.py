print('=' * 20)
print('10 Termos de uma PA')
print('=' * 20)
p1 = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
decimo = p1 + (10 - 1) * rz
for c in range(p1, decimo, rz):
    print('{}'.format(c, end=' '))
print('Acabou')