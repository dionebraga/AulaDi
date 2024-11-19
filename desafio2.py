'''Desafio: Faça um código que permita, ao inserir um valor, o retorno de 5 outputs, sendo eles:
'''

valor = int(input("Insira um valor inteiro: "))
#primeiro output: deve apresentar como resultado o dobro do valor inserido;
dobro = valor*2

print(f"O dobro do valor inserido é: {dobro}")

#segundo output: deve apresentar como resultado o triplo do valor inserido;

triplo = valor*3
print(f"O triplo do valor inserido é: {triplo}")

#terceiro output: deve apresentar como resultado o valor inserido ao quadrado;
potencia = valor**2
print(f"O valor elevado ao quadrado é: {potencia}")

#quarto output: deve apresentar como resultado a raiz quadrada do valor inserido;
raiz_quadrada = valor**(1/2)
print(f"A raiz quadrada do valor inserido é: {raiz_quadrada}")

#quinto output: deve apresentar como resultado a raíz cúbica do valor inserido.

raiz_cubica = valor**(1/3)
print(f"A raiz cúbica do valor inserido é: {raiz_cubica}")