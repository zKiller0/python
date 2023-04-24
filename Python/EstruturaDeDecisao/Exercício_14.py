# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de 
# um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:

n1 = int ( input ( 'Digite a primeira nota: ' ) )
n2 = int ( input ( 'Digite a segunda nota: ' ) )

media = ( n1 + n2 ) / 2

if media >= 9.0:
    conceito = 'A'

elif media >= 7.5:
    conceito = 'B'

elif media >= 6.0:
    conceito = 'C'

elif media >= 4.:
    conceito = 'D'

elif media >= 0:
    conceito = 'E'

if conceito == 'A' or 'B' or 'C':
    resultado = 'Aprovado!' 

elif conceito == 'D' or 'E':
    resultado = 'Reprovado!'

print ( 'Nota 1: %.2f \nNota 2:%.2f' % ( n1 , n2 ) ) 
print ( 'Média: %.2f' % media )
print ( 'Conceito:%s' % conceito )
print ( 'Resultado:%s' % resultado )   