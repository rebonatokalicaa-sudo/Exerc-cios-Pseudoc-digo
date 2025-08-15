numero = input("Digite um número para visualizar a tabuada: ")
numero = int(numero)

i = 1
while i <= 10:
    print(numero, "x", i, "=", numero * i)
    i = i + 1
