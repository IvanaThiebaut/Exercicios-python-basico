sal = float(input('Qual é o salário do funcionário? R$ '))
if sal <= 1250:
    aumento = sal * 0.15
    print('O aumento será de 15%, que aumentará R$ {:.2f} no seu salário, passando a ser R$ {}.'.format(aumento, (sal+aumento)))
else:
    aumento = sal * 0.10
    print('O aumento será de 10%, que aumentará R$ {:.2f} no seu salário, passando a ser R$ {}.'.format(aumento, (sal + aumento)))
