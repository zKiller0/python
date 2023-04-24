# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
''''
par ou ímpar;
positivo ou negativo;
inteiro ou decimal
'''

num1 = int ( input ( 'Digite um número: ' ) )
num2 = int ( input ( 'Digite outro número: ' ) )

#Função que soma os dois números digitados
operacao = int ( input ( '(1-Adição) (2-Subtração) (3-Multiplicação) (4-Divisão)'  ) )

if operacao == 1:
    result = num1 + num2
elif operacao == 2:
    result = num1 - num2
elif operacao == 3:
    result = num1 * num2
elif operacao == 4:
    result = num1 / num2
else:
    print ( 'Operação inválida' )
    exit()

print ( 'Resultado: %d.' % result )