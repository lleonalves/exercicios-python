v1 = float(input('Digite a velocidade do carro: '))
print('Velocidade permitida pela rodovía é de até 80km/h\nAnalisando...')
multa = (v1-80)*7
if v1 <= 80.0:
    print('Você está dentro do permitido')
else:
    print('Você ultrapassou a velocidade e receberá uma multa de R$7,00 por km acima do limite, totalizando R${:.2f}'.format(multa))
print('Drive Safely :)')