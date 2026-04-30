def calcular_financiamento():
    print("--- Sistema de Financiamento ---")
    
    # 1. Entrada de dados
    try:
        valor_compra = float(input("Digite o valor total da compra: R$ "))
        num_parcelas = int(input("Digite a quantidade de parcelas (2, 4, 6 ou 8): "))

        # 2. Tabela de Juros (Dicionário: Parcelas -> Porcentagem)
        tabela_juros = {
            2: 3,
            4: 7,
            6: 9,
            8: 12
        }

        # 3. Processamento
        if num_parcelas in tabela_juros:
            porcentagem = tabela_juros[num_parcelas]
            
            # Cálculo do montante total com juros simples
            valor_total = valor_compra * (1 + porcentagem / 100)
            valor_parcela = valor_total / num_parcelas

            # 4. Saída formatada
            print(f"\nResumo da Operação:")
            print(f"- Juros aplicados: {porcentagem}%")
            print(f"- Valor total financiado: R$ {valor_total:,.2f}")
            print(f"- Valor de cada parcela ({num_parcelas}x): R$ {valor_parcela:,.2f}")
        else:
            print("\nErro: A quantidade de parcelas informada não consta na nossa tabela de juros.")
            print("Opções aceitas: 2, 4, 6 ou 8.")

    except ValueError:
        print("\nErro: Por favor, insira valores numéricos válidos.")

# Executar o programa
if __name__ == "__main__":
    calcular_financiamento()
    