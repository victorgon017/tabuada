#entrada de dados
numero = int(input("Digite um número de 1 a 10 e veja a sua tabuada completa: "))
#processamento
for i in range (11):
    print (numero, "x", i, "=", numero * i)