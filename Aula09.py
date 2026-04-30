from random import shuffle
seleçoes = ['Brasil' , 'Argentina' , 'Paraguai' , 'Chile' , 'Bolivia' , 'Alemanha' , 'Espanha' , 'Portugal']

shuffle(seleçoes)
jogos = []
while seleçoes:
    time1 = seleçoes.pop()
    time2 = seleçoes.pop()
    jogos.append((time1,time2))
    
for i, jogo in enumerate(jogos):
    print(f'{i} - {jogo[0]} x {jogo[1]}')
    