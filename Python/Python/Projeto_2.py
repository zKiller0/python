# Chute um número
''''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10
e permite que o usuário chute um número até que o valor aleatótio gerado no 
início do programa seja chutado corretamente.

input valor_aleatorio
input 'chute um numero'
if chute > valor_aleatorio
 print 'Chute foi maior que o valor gerado'
if chute < valor_aleatorio
 print 'Chute foi menor que o valor gerado'
if chute = valor_aleatorio
 print 'Você acertou!'
'''

import random 

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10:  '))
    if chute > valor_aleatorio:
       print('Chute maior que o valor gerado')
    elif chute < valor_aleatorio:
       print('Chute menor que o valor gerado')
    elif chute == valor_aleatorio:
       acertou = True
    print('Você acertou!')

        