times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense',
         'Bragantino', 'Athletico', 'Fortaleza', 'Atlético MG',
         'Cuiaba', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional',
         'Goias', 'Bahia','Santos', 'Vasco', 'America-Mg', 'Coritiba')
print('-=' * 30)
print(f'Lista dos times do brasileirão: {times}')
print('-=' * 30)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-=' * 30)
print(f'Os 4 ultimos colocados são {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
pos_galo = times.index('Atlético MG', 0, 21) + 1
print(f'O Atlético mineiro está em {pos_galo}°')
