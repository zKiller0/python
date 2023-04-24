# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% 
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
''''
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

# Entrada de dados
valor_hora = int ( input ( 'Quanto ganha por hora? ') )  
horas_trabalhadas = int ( input ( 'Quantas horas trabalha por mês? ' ) )

# Cálculos
salario_bruto = valor_hora * horas_trabalhadas
IR = salario_bruto * 0,11
INSS = salario_bruto * 0,8
sindicato = salario_bruto * 0,5
salario_liquido = salario_bruto - IR - INSS - sindicato 

# Mostrando na tela
print ( '' )
print ( 'Salário Bruto: R$%.2f' % salario_bruto)                # Não consegui achar o erro
print ( 'Descontos' )
print ( 'IR: R$%.2f ' % IR ) 
print ( 'INSS: R$%.2f' % INSS )
print ( 'Sindicato: R$%.2f' % sindicato )
print ( '' )
print ( 'Salário Líquido: R$%.2f' % salario_liquido )