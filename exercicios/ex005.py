w = float(input('Largura da parede:'))
h = float(input('Altura da parede:'))
print('Sua parede tem a dimensão de {}m²x{}m², a área da sua parede é de {:.2f}m², portanto você precisará de {:.0f}l de tinta no total'.format(w,h,w*h,(w*h)/2))
