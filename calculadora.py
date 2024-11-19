num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))

operacao = input("Insira a operação que deseja realizar: ")

if operacao == "multiplicar" :
    print(num1*num2)

elif operacao == "somar" :
    print(num1+num2)

elif operacao == "dividir" :
    print(num1/num2)

elif operacao == "subtrair" :
    print(num1-num2)

elif operacao == "potencializar" :
    print(num1**num2)