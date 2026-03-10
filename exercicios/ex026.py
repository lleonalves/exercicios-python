viagem = float(input('Qual é a distância da sua viagem em km? '))
p1 = viagem * 0.50
p2 = viagem * 0.45
if viagem <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(p1))
else:
    print('O preço da sua viagem será de R${:.2f}'.format(p2))