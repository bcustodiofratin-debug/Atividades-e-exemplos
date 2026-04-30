import random
import time 
import subprocess

subprocess.run("cls",shell=True)

def mostra_senha(indice,digitos):
    if indice == 0:
        return "____"
    elif indice == 1:
        return f"{digitos[0]}___"
    elif indice == 2:
        return f"{digitos[0]}{digitos[1]}__"
    elif indice == 3:
        return f"{digitos[0]}{digitos[1]}{digitos[2]}_"
    else:
        return f"{digitos[0]}{digitos[1]}{digitos[2]}{digitos[3]}"

#Gera senha de 4 digitos (como string)
digitos = str(random.randint(0,9999)).zfill(4)

indice = 0
tentativas = 0
tempo_inicial = time.time()

print("Confer Digital, tente adivinhar a senha de 4 digitos!")
print(mostra_senha(indice,digitos))

#núcleo do código
while indice < 4:
    tentativas += 1
    digito = int(digitos[indice])
    chute = int(input(f"Digite o {indice + 1}° digito: "))
    
    if digito > chute:
        print("O digito é maior!")
    elif digito < chute:
        print("O digito é menor!")
    else:
        print("Digito correto!!!")
        indice +=1
        input("ENTER para continuar")
        subprocess.run("cls",shell=True)
        print(mostra_senha(indice,digitos))

tempo_total =  time.time() - tempo_inicial 

print("\n🔓 COFRE ABERTO!!!")
print(f"Senha: {digitos}")
print(f"Tentativas: {tentativas}")
print(f"Tempo: {tempo_total:.2f} Segundos")