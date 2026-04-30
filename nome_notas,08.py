
nome = []
notas = []
x = int(input('Digite a quantidade de alunos: '))

for i in range(x):
    nomes = input(f'Digite seu nome do {i+1}º aluno: ')
    nota = input(f'Digite a nota do(a) aluno(a) {nomes}: ')
    nome.append(nomes)
    notas.append(nomes)

while True: 
    n = int(input(f'Digite o indice do aluno (0-{x - 1}): '))
    if n >=0 and n <x: break

print(f' A nota do aluno {nomes[n]} é {notas[n]}')

nome = input('Digite o nome do aluno: ')
if nome in nomes:
    indice = nomes.index(nome)
    print(f'A nota do aluno {nomes[indice]} é {notas[indice]}') 
    