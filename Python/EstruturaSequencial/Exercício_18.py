# Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
# a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download
#  do arquivo usando este link (em minutos).

mb = int ( input ( 'Digite o tamanho do arquivo em MB: ' ) )
mbps = int ( input ( 'Digite a velocidade do link em Mbps: ' ) ) 

tempo = ( ( mb * 8 ) / mbps ) / 60

print ( 'O tempo aproximado de download é de: %.2f minutos' % tempo )

