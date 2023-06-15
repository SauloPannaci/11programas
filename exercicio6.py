while True:
    identificacao = input("Digite o número de identificação do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media_exercicios = float(input("Digite a média dos exercícios: "))

    media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

    conceito = ''
    if media_aproveitamento >= 9.0:
        conceito = 'A'
    elif 7.5 <= media_aproveitamento < 9.0:
        conceito = 'B'
    elif 6.0 <= media_aproveitamento < 7.5:
        conceito = 'C'
    elif 4.0 <= media_aproveitamento < 6.0:
        conceito = 'D'
    else:
        conceito = 'E'

    resultado = "REPROVADO"
    if conceito in ['A', 'B', 'C']:
        resultado = "APROVADO"

    print("Número do Aluno:", identificacao)
    print("Notas: {nota1}, {nota2}, {nota3}")
    print("Média dos Exercícios:", media_exercicios)
    print("Média de Aproveitamento:", media_aproveitamento)
    print("Conceito:", conceito)
    print("Resultado:", resultado)

    opcao = input("Deseja digitar as notas de outro aluno? (S/N): ")
    if opcao.upper() != 'S':
        break