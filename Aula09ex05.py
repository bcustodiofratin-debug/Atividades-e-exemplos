alunos = set()


n = int(input('Digite a quantidade de entrada: '))

for _ in range(n):
    nome = input('Digite o nome do aluno: ')
    alunos.add(nome)
    
print('Alunos cadastrados: ')

for nome in alunos: 
    print(nome)
    
print(f'Quantidades de alunos unicos: {len(alunos)}')
