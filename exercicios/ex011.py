# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimentoo da hipotenusa.
from math import hypot
c1 = float(input('Digite o valor do cateto oposto:'))
c2 = float(input('Digite o valor do cateto adjacente:'))
h = hypot(c1, c2)
print('O cateto oposto é {}, o cateto adjacente é {}, sendo assim, a hipotenusa só pode ser {:.2f}'.format(c1, c2, h))
