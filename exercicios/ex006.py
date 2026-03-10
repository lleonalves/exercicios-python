p = float(input('Qual é o preço do produto? R$'))
d = 5
t = p*d/100
sale = p - t
print('O produto custava R${:.2f}, na promoção ele ganhou 5% de desconto, portanto passou a custar R${:.2f}'.format(p,sale))
