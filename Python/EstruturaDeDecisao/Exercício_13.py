# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

semana = int ( input ( 'Digite um número entre 1 e 7: ' ) )

if semana == 1:
    print ( '->Domingo' )

elif semana == 2:
    print ( 'Segunda' )

elif semana == 3:
    print ( 'Terça' )

elif semana == 4:
    print ( 'Quarta' )

elif semana == 5:
    print ( 'Quinta' )

elif semana == 6:
    print ( 'Sexta' )

elif semana == 7:
    print ( 'Sábado' )

else:
    print ( 'Valor inválido' )
