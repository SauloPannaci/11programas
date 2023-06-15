total_avaliacoes = int(input("Digite o total de avaliações: "))
soma_notas = 0

for i in range(1, total_avaliacoes + 1):
    nota = float(input(f"Digite a nota da avaliação {i}: "))
    soma_notas += nota

media = soma_notas / total_avaliacoes
print("A média das notas é:", media)





