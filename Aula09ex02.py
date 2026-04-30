dias = ('dom','seg','ter','qua','qui','sex','sab')

hoje = input('Que dia e hoje ?')
qt_dias = int(input('Quantos dias pra o evento ?'))

evento = (dias.index(hoje) + qt_dias)%7

print(f'O evento sera : {dias[evento]}')
