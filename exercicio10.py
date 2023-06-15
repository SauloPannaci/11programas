n = int(input("Digite a quantidade de números: "))

for i in range(n):
    numero = float(input("Digite o número {}: ".format(i+1)))

    if numero > 0:
        print("Número {} é positivo.".format(numero))
    elif numero < 0:
        print("Número {} é negativo.".format(numero))
    else:
        print("Número {} é zero.".format(numero))