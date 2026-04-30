bin = input('Digite um numero binario: ')
n = len(bin) - 1

decimal = 0


for dig in bin:
    decimal += int(dig)*2**n
    n -= 1
print(f'O binario {bin} equivale o decimal {decimal}')