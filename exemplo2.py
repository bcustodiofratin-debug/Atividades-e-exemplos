#digito = int(input('Qual o final da placa? '))
placa = input('Digite a placa com 8 caracteres: ')

if len(placa) >8:
    print('palca invalida')
else:
    digito = int(placa[7])

match digito:
    case 1 | 2:print('Não pode rodar segunda feira')
    case 3 | 4:print('Não pode rodar terça feira')
    case 5 | 6:print('Não pode rodar quarta feira')
    case 7 | 8:print('Não pode rodar quinta feira')
    case 9 | 0:print('Não pode rodar sexta feira')
    case _: print('Digito invalido')
    
   