''''
valor = float(input('Digite um valor da compra: ')) 
qt_parcelas = (int(input('Digite uma parcela(2/4/6/8): ')))

if qt_parcelas == 2: juro = 3
elif qt_parcelas == 4: juro = 7
elif qt_parcelas == 6: juro = 9
elif qt_parcelas == 8: juro = 12
else: juro = -1

if juro <0:
    print(f'Invalido')
else:
    valor = valor + valor * juro/100
    parcela= valor / qt_parcelas
    print(f'Valor total R${valor:.2f}\n{qt_parcelas} de R${parcela:.2f}')
'''
'''
match qt_parcelas:
    case 2:juro = 3
    case 4: juro = 7
    case 6: juro =9
    case 8: juro = 12
    case _: juro = -1
'''