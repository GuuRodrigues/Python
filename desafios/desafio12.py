salario = float(input('Digite o salario do funcionário: '))
aumento = (salario*0.15)+salario

print('Com o reajuste o sálario de {}R$ foi para {:.2f}R$'.format(salario, aumento))