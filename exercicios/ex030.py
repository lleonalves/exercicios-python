a = float(input('Digite um segmento de reta: '))
b = float(input('Digite outro segmento de reta: '))
c = float(input('Digite mais um segmento de reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos {}, {} e {} PODEM FORMAR um triângulo!'.format(a,b,c))
else:
    print('Os segmentos {}, {} e {} NÂO PODEM FORMAR um triângulo!'.format(a,b,c))