# Laços de repetição

for palavra in range(1,4):
      print('Carregando')

''''
for item in coleção:
    expressão
'''
''''
for item in range(1,21):  
       print(item)

for item in range(1,20,2):
    print(item)

nomes = ['Ricardo', 'Italo', 'Marcos', 'Felipe']

for nome in nomes:
    print(nome)
'''

# Input número máximo
# valor inicial = 1
# loop de valor_inicial a numero_maximo
# print valor10

valor_maximo = int(input('Digite o valor máximo'))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo + 1):
    print(numero)