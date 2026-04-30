num = int(input('Digite um decimal: '))
binario = ''

while num > 0:
    dig = num 
    num = num//2
    binario = str(dig) = binario
    num = num//2
    
print(f'O decimal {num} equivale ao binario {binario}')