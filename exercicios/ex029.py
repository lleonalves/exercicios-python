sal = float(input('Digite o seu salário: R$ '))
if sal <= 1250:
    print('Seu aumento será de 15%, totalizando R$ {:.2f}'.format(sal * 15/100 + sal))
else:
    print('Seu aumento será de 10%, totalizando R$ {:.2f}'.format(sal * 10/100 + sal))