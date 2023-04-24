# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
''''
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
'''
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

acumulador = 0

resposta = input 
( "Telefonou para a vítima?" )
if resposta.lower () == 's':
    acumulador += 1


resposta = input ( "Esteve no local do crime?" )
if resposta.lower () ==  's':
    acumulador += 1

resposta = input ( "Mora perto da vítima?" )
if resposta.lower () == 's':
    acumulador += 1

resposta = input ( "Devia para a vítima?" )
if resposta.lower () == 's':
    acumulador += 1

resposta = input ( "Já trabalhou com a vítima?" )
if resposta.lower () == 's':
    acumulador += 1

if acumulador < 2:
    print ( 'Inocente' )

elif acumulador == 2: 
    print ( 'Suspeito' )

elif acumulador == 3 and acumulador < 4:
    print ( 'Cúmplice' )

elif acumulador < 5:
    print ( 'É o assasino' )
    





