alt = float(input('Digite a altura da sua parede: '))
lar = float(input('Digite a largura da sua parede: '))
area = alt*lar
tinta = area/2
print('Largura da parede: {}'.format(lar))
print('Altura da parede: {}'.format(alt))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(alt, lar, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
