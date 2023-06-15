for i in range(75):
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    
    if idade >= 18:
        print("Pessoa {} é maior de idade.".format(i+1))
    else:
        print("Pessoa {} é menor de idade.".format(i+1))