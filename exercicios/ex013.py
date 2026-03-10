#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
a = str(input('Digite o nome do aluno 1:'))
b = str(input('Digite o nome do aluno 2:'))
c = str(input('Digite o nome do aluno 3:'))
d = str(input('Digite o nome do aluno 4:'))
lista = [a,b,c,d]
print('O nome escolhido foi: {}'.format(random.choice(lista)))
