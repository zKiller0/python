# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
''''
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

n1 = int ( input ( 'Nota 1: ' ) )
n2 = int ( input ( 'Nota 2: ' ) )
n3 = int ( input ( 'Nota 3: ' ) )

media = ( n1 + n2 + n3 ) / 3

if media >= 7.0:
    print ( 'Aprovado')
elif media < 7.0:
    print ( 'Reprovado' )
else:
     media == 10.0
     print ( 'Aprovado com distinção' )
  