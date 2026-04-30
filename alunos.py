alunos = int(input('Digite a quantidade de alunos: '))
mais_alto = 0
soma = 0

for i in range(alunos):
    altura = float(input(f'Digite o {i+1}° numero: '))
    soma += altura
    if altura > mais_alto:
        mais_alto = altura
    
    
media = soma/altura

print(f'a media dos alunos é: {media:.2f}')
print(f'O aluno mais alto dessa turma tem {mais_alto:.2f}')
