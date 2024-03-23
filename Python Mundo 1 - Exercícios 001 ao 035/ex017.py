import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente'))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir {}'.format(hi))