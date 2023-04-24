# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

n1 = int ( input ( 'Digite um número inteiro: ' ) )

n2 = int ( input ( 'Digite um número inteiro: ' ) )

n3 = int ( input ( 'Digite um número real: ' ) )

print ( 'Soma: ' , ( ( 2 * n1 )  * ( n2 / 2 ) ) )

print ( 'Produto: ' , ( 3 * n1 ) + n3 ) 

print ( 'Cubo: ' , n3 ** 3 )