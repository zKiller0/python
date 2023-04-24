# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = int ( input ( 'Insira seu salário: ' ) )

if ( salario <= 280 ):
    percentual = 20
elif ( salario <= 700 ):
    percentual = 15
elif ( salario <= 1500 ):
    percentual = 10
else:
    percentual = 5

print ( f'Salário original:R${salario}')
print ( f'Percentual:{percentual}', '%' )

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento

print ( f'Aumento:R${aumento}' )
print ( f'Novo salário:R${novo_salario}' )


