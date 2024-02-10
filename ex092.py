from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contrataçao'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contrataçao'] + 35) - datetime.now().year
print('-=' * 20)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')