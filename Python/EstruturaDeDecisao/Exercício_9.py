# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int ( input ( 'Digite o primeiro número: ' ) )
n2 = int ( input ( 'Digite o segundo número: ' ) )
n3 = int ( input ( 'Digite o terceiro número: ' ) )

print("")

print (n1 , n2, n3)

# Algoritmo:
# 1. Compara as duas últimas posições
# 2. Compara as duas primeiras posições
# 3. Compara novamente as duas últimas posições

if ( n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux
if ( n2 > n1 ):
    aux = n2
    n2 = n1
    n1 = aux
if ( n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux
   
print ( f'Exibindo em ordem decrescente:{n1} {n2} {n3}')