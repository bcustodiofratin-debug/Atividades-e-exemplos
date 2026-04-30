def media(num1,num2):
    return(num1 + num2)/2

def diferença(num1,num2):
    if num1 < num2:
        return num2 - num1
    else:
        return num1 - num2
def produto(num1,num2):
    return num1 * num2

def divisão(num1,num2):
    if num2 ==0:
        print('Não é possivel dividir por zero')

while True: 
    print('[1] Média\n[2] Diferença entre o maior e o menor')
    print('[3] Produto\n[4] Divisão do primeiro pelo segundo')
    print('[5] Sair')
    op = int(input('Digite um opção: '))
    if op == 5: break
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    match op:
        case 1: print(f'A media dos numero é {media(num1, num2)}')
        case 2: print(f'A distançia entre os numeros é {diferença(num1, num2)}')
        case 3: print(f'O produto entre os numeros é {produto(num1, num2)}')
        case 4: divisão(num1,num2)
        case _: print('Opção invalida')