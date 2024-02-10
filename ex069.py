pessoasmaiores = homens = mulheres = totmulher20 = 0
idade = 0
r = 'S'
print('-' * 5, 'CADASTRE UMA PESSOA', '-' * 5)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]' )).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'F':
        mulheres += 1
        if idade <= 20:
            totmulher20 += 1
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        pessoasmaiores +=1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'A quantidade de pessoas com mais de 18 anos é de {pessoasmaiores} pessoas')
print(f'Foram cadastrados {homens} homens.')
print(f'Temos {totmulher20} mulheres menores de 20 anos.')
