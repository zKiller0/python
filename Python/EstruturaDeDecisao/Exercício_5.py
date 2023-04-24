# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nt1 = int ( input ( ' Insira a nota 1: ' ) )
nt2 = int ( input ( ' Insira a nota 2: ' ) )

media = ( nt1 + nt2 ) / 2
print ( f'Sua média é: {media}')

if media >= 7.0:
    print ( 'Aprovado' )
elif media < 7.0: 
    print ( 'Reprovado' )
else: 
    media = 10.0
    print ( 'Aprovado com Distinção' )