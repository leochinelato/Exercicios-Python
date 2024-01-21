times = (
    'Palmeiras',
    'Botafogo',
    'Atlético-MG',
    'Flamengo',
    'Grêmio',
    'Bragantino',
    'Fluminense',
    'Athletico-PR',
    'São Paulo',
    'Internacional',
    'Fortaleza',
    'Cuiabá',
    'Corinthians',
    'Cruzeiro',
    'Santos',
    'Vasco da Gama',
    'Bahia',
    'Goiás',
    'Coritiba',
    'América-MG',
)

print('-=' * 25)
print(f'Times do Brasileirão: {times}')
print('-=' * 25)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' * 25)
print(f'Os 4 ultimos times são: {times[-4:]}')
print('-='*25)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*25)
print(f'O Fortaleza está na {times.index("Fortaleza")+1}ª posição')