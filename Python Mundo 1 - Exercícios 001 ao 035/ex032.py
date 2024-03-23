import calendar
ano = int(input('Qual ano você deseja saber se é bissexto?'))
bissexto = calendar.isleap(ano)
if bissexto == True:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
