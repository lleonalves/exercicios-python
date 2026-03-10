salario = float(input('Qual é o seu sálario?R$'))
aumento = salario + (salario*15/100)
print('O seu sálario era de R${:.2f} e passou a ser R${:.2f} após o aumento.Aproveite!'.format(salario,aumento))
