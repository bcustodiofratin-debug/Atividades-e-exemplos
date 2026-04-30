alunos = []

x = int(input('Digite a quantidade de alunos: '))

for i in range(x):
    nomes = input(f'Digite seu nome do {i+1}º aluno: ')
    nota1 = float(input(f'Digite a 1º nota do {nomes}: '))
    nota2= float(input(f'Digite a 2º nota do {nomes}: '))
    media = (nota1 + nota2)/2
    
print(10*'-')
while True:
    n = int(input('Digite a quantidade de alunos: '))
    if n>=0 and n<len(alunos):
        break
    
result = 'Aprovado' if alunos[n][1] >= 6.0 else 'Reprovado'
print(f'O aluno {[n][0]} foi {result} com media {alunos[n][1]:.2f}')