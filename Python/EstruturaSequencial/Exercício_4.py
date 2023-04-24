# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1 = int ( input ( ' Insira a nota 1 ' ) )
nota_2 = int ( input ( ' Insira a nota 2 ' ) )
nota_3 = int ( input ( ' Insira a nota 3 ' ) )
nota_4 = int ( input ( ' Insira a nota 4 ' ) )

# Divisão das notas para conseguir a média
media = float ( nota_1 + nota_2 + nota_3 + nota_4 ) / 4
print ( f'A media é: {media} ' )