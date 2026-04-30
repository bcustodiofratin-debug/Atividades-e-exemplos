'''
nomes = []

x= int(input('Digite o nome do aluno: '))
for i in range(x):
    nome = input (f'Digite o nome do {i+1}º aluno: ')
    
for i, nome in enumerate(nomes,start=1):
    print(f'[{i}] - {nomes}')
'''
itens = ['soma', 'subtração', 'divisão', 'multiplicação']

for i, item in enumerate(itens,start=1):
    print(f'[{i}] - {item}')