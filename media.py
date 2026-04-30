soma = 0
n = int(input('Digite a quantidade de númrtos: '))

for i in range(n):
    num = float(input(f'digite o {i+1}° numero:'))
    soma += num
    

media = soma/n
print(f'A media dos numeros é {media:.2f}')
