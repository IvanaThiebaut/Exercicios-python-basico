from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('O atleta tem {} anos, ele é da categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, ele é da categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos, ele é da categoria JUNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos, ele é da categoria SENIOR.'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos, ele é da categoria MASTER.'.format(idade))
