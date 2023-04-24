# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois 
# informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
''''
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, 
uma nota de 5 e quatro notas de 1.

'''
valor_saque = int ( input ( 'Valor para sacar [10 - 600]: ' ) )

cem = int ( valor_saque / 100 )
valor_saque = valor_saque - ( cem * 100 ) 

cinquenta = int ( valor_saque / 500 )
valor_saque = valor_saque - ( cinquenta * 50 )

dez = int ( valor_saque / 10 )
valor_saque =  valor_saque - ( dez * 10 )

um = valor_saque

print ( 'Notas R$100,00 = ' , cem )
print ( 'Notas R$ 50,00 = ' , cinquenta )
print ( 'Notas R$ 10,00 = ' , dez )
print ( 'Notas R$ 1,00 = ' , um)