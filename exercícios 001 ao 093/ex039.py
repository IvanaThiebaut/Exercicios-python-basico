ano = int(input('Qual o ano do seu nascimento? '))
print('Quem nasceu no ano {} deve se alistar em {}'.format(ano, (ano + 18)))
atual = 2023
idade = atual - ano
if idade < 18:
    print('Você ainda não deve se alistar. Seu alistamento será em {} anos.'.format(18 - idade))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
elif idade == 18:
    print('Esse é o seu ano de alistamento.')