print('-=-' * 20 )
print('Olá Mãe, Bem vindo ao meu Progama!')
# aqui fiz um progama para ajustar as finanças de casa!
# poderia sim ter usado outras funções, mas minha querida mãe quis assim
salario = ---- #decidi não mostrar o salário, pois é um valor fixo e não muda!
n1=float(input('Digite o valor do Dízimo: '))
n2=float(input('Digite valor da oferta: '))
n3=float(input('Digite o gasto com a escola: '))
n4=float(input('Digite o gasto com a net: '))
n5=float(input('Digite o gasto com a luz: '))
n6=float(input('Psicopedagoga do Felipe: '))
n7=float(input('Banco(Juros, Netflix e tarifas): '))
n8=float(input('O gasto da gasolina: '))
n9=float(input('O gasto do Banco Lis: '))
n10=float(input('O gasto com o Ônibus: '))
n11=float(input('O gasto com a farmácia: '))
n12=float(input('Gás da cozinha: '))
n13=float(input('Cartão de crédito: '))
n14=float(input('Mercado: '))

soma=n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14

resultado = salario - soma

if salario >= soma:
    print('Parabéns! Você economizou R${}!   '.format(resultado))

else:
    print('Fica devendo R${} Mãe! '.format(resultado))
print('-=-' * 20 )
