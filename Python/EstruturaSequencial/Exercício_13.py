# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

h = int ( input ( 'Digite a altura do homem: ' ) )
f = int ( input ( 'Digite a altura da mulher: ' ) )

valor_1 = ( h * 72.7 )
valor_2 = ( valor_1 - 58 )

print ( f'o peso do homem é:{valor_2}')

valor_3 = ( f * 62.1)
valor_4 = ( valor_3 - 44.7 )

print ( f'O peso ideal da mulher é:{valor_4}' ) 