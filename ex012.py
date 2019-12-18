n1 = float(input('Nota do 1 aluno: '))
n2 = float(input('Nota do 2 aluno: '))
media = (n1 + n2)/ 2
print('A média do aluno é de {}' .format(media))
if media >= 5 and media < 6:
    print('Com essa média {}, você está de recuperação!' .format(media))
elif media < 5:
    print('O aluno está reprovado!')
elif media >= 6:
    print('O aluno foi aprovado!')
