def calcular_lucro_prejuizo(preco_custo, preco_venda):
    if preco_venda > preco_custo:
        return "Lucro"
    elif preco_venda < preco_custo:
        return "Prejuízo"
    else:
        return "Empate"

total_precos_custo = 0
total_precos_venda = 0

for i in range(1, 41):
    print(f"\nProduto {i}:")
    preco_custo = float(input("Digite o preço de custo: "))
    preco_venda = float(input("Digite o preço de venda: "))

    resultado = calcular_lucro_prejuizo(preco_custo, preco_venda)
    print("Resultado:", resultado)

    total_precos_custo += preco_custo
    total_precos_venda += preco_venda

media_precos_custo = total_precos_custo / 40
media_precos_venda = total_precos_venda / 40

print("\n=== Média dos Preços ===")
print("Média de Preço de Custo:", media_precos_custo)
print("Média de Preço de Venda:", media_precos_venda)