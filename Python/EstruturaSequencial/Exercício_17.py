# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
# sempre arredonde os valores para cima, isto é, considere latas cheias.

metros = int ( input ( 'Informe os metros quadrados: ' ) )
litros = metros / 6

if (metros%108 > 0 and metros%21.6 > 0. ):
 latas = metros // 108
 latas = latas + 1
 precol = latas * 80
 galao = metros // 21.6
 galao = galao + 1
 precog = galao * 25

 print ( 'Você vai precisar apenas de: {} latas de 18L e vai gastar {} reais' .format ( latas , precol ) )
 print ( 'Você vai precisar apenas de {} galao de 3,6L e vai gasta {} reais' .format ( galao , precog ) )
 