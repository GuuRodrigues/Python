larg = float(input('Qual a altura da parede: '))
alt  = float(input('Qual a largura da parede: '))
area = larg*alt
litros = area/2

print('A área dessa parede é igual a {:.2f} metros quadrados para pintá-la será necessário {} litros de tinta'.format(area, litros))