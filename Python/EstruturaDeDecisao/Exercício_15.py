# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#  Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
''''
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''
a = int ( input ( 'Digite um valor para o lado 1: ' ) )
b = int ( input ( 'Digite um valor para o lado 2: ' ) )
c = int ( input ( 'Digite um valor para o lado 3: ' ) )

# Testando se é um triângulo 

if ( a + b < c) or ( a + c < b ) or ( b + c < a ): 
    print ( 'Não é um triângulo!' )
elif ( a == b ) and ( a == c ):
    print ( 'Equilatero' )
elif ( a == b ) or ( a == c ) or ( b == c ):
    print ( 'Isósceles' )
else:
    print ( 'Escaleno' )
