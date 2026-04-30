alunos = {}
disciplinas = ('Prog.computação' , 'Eng. prompt' , 'prototipagem')
n = int(input('Digite a quantidade de aluno: '))

for i in range(n):
    nome = input(f'Digite o nome do {i + 1}º aluno: ').capitalize()
    alunos[nome] = []
    for disc in disciplinas:
        nota = float(input(f'Digite a nota de {disc}: '))
        alunos[nome].append(nota)
        
print(alunos)

while True : 
    nome = input('Digite o nome do aluno (Enter pra sair): ').capitalize()
    if len(nome) == 0:break
    if nome in alunos: 
        print(f'NOtas do aluno {nome} ')
        for i, disc in enumerate(disciplinas):
            print(f'{disc}: {alunos[nome][i]:.2f}')
    else:
        print(f'Aluno {nome} não encontrada!')
        
