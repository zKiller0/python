# Faça um Programa que peça dois números e imprima a soma.

def sum ( num1 , num2 ) : # Função que soma os dois números digitados
    return num1 + num2

# Atribui valores nas variáveis
print ( " /t Soma de dois números /n " )
num1 = int ( input ( 'Insira um número: ' ) )
num2 = int ( input ( 'Insira outro número: ' ) )

# Imprime resultado na tela
print ( "O resultado da some é %d" % sum ( num1 , num2 ) )
