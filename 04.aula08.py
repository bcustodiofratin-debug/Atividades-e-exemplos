alunos = []
soma = 0

x = int(input('Digite a quantidade de alunos: '))

for i in range(x):
    nomes = input(f'Digite seu nome do {i+1}º aluno: ')
    nota = float(input(f'Digite a nota do(a) aluno(a) {nomes}: '))
    alunos.append((nomes,nota))
    soma += nota
    
media = soma/x
print(f'A media da turma é {media:.2f} ')

for nome, nota in alunos:
    if nota > media:
        print(f'Parabens {nome} sua nota esta cima da media!')