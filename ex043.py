peso = float(input('Qual seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
print('Seu IMC é {}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso indicado.')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está obeso.')
elif imc > 40:
    print('Você está com obesidade morbida.')