km = float(input('Quantos km foi percorrida pelo carro?'))
dias = int(input('Quantos dias foram alugados?'))
preço = (km*0.15)+(dias*60)
print('Você percorreu {}km por {} dias, portanto deve pagar R${:.2f}'.format(km,dias,preço))
