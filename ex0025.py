nome = str(input('Digite seu nome completo')).strip()
n = nome.upper()
s = 'SILVA' in n
if s == True:
    print('Essa pessoa tem Silva no nome')
else:
    print('Essa pessoa não tem Silva no nome')