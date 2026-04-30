nomes = []
pontuacao = []

n = int(input('Digite a quantidade de alunos: '))

for i in range(n):
    nome = input('Digite o nome: ')
    pontos = float(input('Digite a pontuação: '))
    nomes.append(nome)
    pontuacao.append(pontos)
    
for nome,pontos in zip(nomes,pontuacao):
    print(f'o aluno {nome} tirou: {pontos}')