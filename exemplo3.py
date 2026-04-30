soma = 1
num = int(input('digite a quantidade de numero: '))

for i in range(1,num+1):
    if i %15 == 0:
        print('fizzbuzz')
    elif i %3 == 0:
        print ('fizz')
    elif i %5 == 0:
        print('buzz')
    elif i %3 == 0 and i %5 == 0:
        print ('fizzbuzz')
    else:
        print(f'{i}')
print (i,end = '')
