# Coleções
''''
preco_1 = 30
preco_2 = 50
preco_3 = 600
'''

# Lista
''''
precos = [30,50,600]
#          0  1  2 
print(precos[1])
print(precos.index(600)) # Encontrar o índicie de algo
'''

# Listas
''''
diversidades = [30,'Ricardo',False]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
'''

# Laços em iteráveis
''''
for preco in precos:
    print('preco')
'''

# Exemplo 5 - Some os valores 
# Dados um a coleção de dados "idades" [15,46,75,34,23]
# imprima na tela a soma destes valores

''''
idades = [15,46,75,34,23]
loop idade em idades
total = total + idade
print total
'''
idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
    print(total)