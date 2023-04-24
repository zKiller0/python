# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

p1 = int ( input ( 'Informe o preço do produto 1: ' ) )
p2 = int ( input ( 'Informe o preço do produto 2: ' ) )
p3 = int ( input ( 'Informe o preço do produto 3: ' ) )

if p1 < p2 and p3:
    print ( 'O primeiro produto é mais barato' )
elif p2 < p3 and p1:
    print ( 'O segundo produto é mais barato')
else:
    p3 < p1 and p2 
    print ( 'O terceiro produto é mais barato' )
