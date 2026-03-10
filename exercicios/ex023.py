from random import randint
from time import sleep
computador = randint(0,5)
perg = int(input('Estou pensando em um número de 0 a 5, qual é esse número? '))
print('Processando.....')
sleep(5)
if perg == computador:
    print('Parabéns, você acertou!')
else:
    print('Tente novamente!')