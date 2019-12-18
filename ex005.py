n1= str(input('Digite o nome de um funcionário: '))
n2= float(input('O número de horas trabalhadas: '))
n3= float(input('O valor que recebe por hora: R$'))
salario= n2 * n3
print('O salário de {} R$ {} ' .format(n1, salario))