# Condicionais

# if elif e else
'''''
e Ae jhonatan, bora dar uma saida hoje?
Se eu terminar meu trabalho aqui, eu consigo.
'''
'''''
trabalho_terminado = False
if trabalho_terminado == True:
    print('Opa!Bora dar uma saida.')
else:
    print('Não posso sair agora.')
    '''

''''
Ei , Você sconsegue me ajudar a mover essas caixas lá pra fora hoje a tarde?
Se  eu estiver livre, sim, se não, pede ao meu irmão para te ajudar
'''
''''
estou_livre = False
if estou_livre == True:
      print('Ok,posso te ajudar.')
else: print('Peça ao meu irmão para te ajudar!')
'''

''''
Eu cheguei na aula atrasado, ainda posso entrar?
Se essa não for a sua terceira vez chegando atrasado, então pode sim,
 caso contrário irá tomar uma suspensão
'''
''''
numero_de_atrasos = 1
if numero_de_atrasos >= 3:
    print('Você está suspenso!') 
elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, será suspenso.')
elif numero_de_atrasos == 2:
    print('Pode entrar, porém caso tome mais 1 falta, será suspenso')
else:
    print('Pode entrar')
'''

# Encontre o maior entre 2 números
''''
input primeiro_valor
input segundo_valor
if primeiro_valo >= segundo_valor
     print o primeiro valor é maior
else
    print o segundo valor é maior
'''

primeiro_valor = input('Digite o 1* valor: ')
segundo_valor = input('Digite o 2* valor: ')

if int(primeiro_valor) > int(segundo_valor):
    print('O primeiro valor é maior')
else: 
    print('O segundo valor é maior')