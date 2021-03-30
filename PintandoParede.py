larg = float(input('Qual é a Largura da parede: '))
alt = float(input('E agora, qual é a Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m² e para pintar essa parede será necessario {}L de tinta'.format(larg, alt, area, tinta))
