contador = 0 
perguntas = ['1-Telefonou para a vitima?' , '2- Esteve no local do crime?' , '3- Mora perto da vitima?'
      '4- Devia dinheiro para vitima?' , '5- Ja trabalho com a vitima?'    ]

for pergunta in perguntas:
    resp = input(f'{pergunta}')
    if resp in "sS":
        contador += 1

if contador == 2:
    print('Suspeito!')
elif contador == 3 or contador == 4:
    print('Cumplice!')
elif contador == 5:
    print('Assasino!')
else:
    print('Inocente!')