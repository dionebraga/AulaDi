peso = float(input("Qual o peso do seu cachorro? "))
banhos = int(input("Quantos banhos seu cachorro tomou no último ano? "))
porte_p = 50
porte_m = 60
porte_g= 75

if peso <= 5:     
    lucro_total = (porte_p - 5) * banhos
    print(f"Olá! Em anos de cachorro, {nome_pet} tem: {idade_real} anos. Tomou {banhos} banhos, gerando R${lucro_total} de lucro!!\n")
    
elif peso <= 10:
    lucro_total = (porte_m - 15) * banhos
    print(f"Olá! Em anos de cachorro, {nome_pet} tem: {idade_real} anos. Tomou {banhos} banhos, gerando R${lucro_total} de lucro!!\n") 

else:
    lucro_total = (porte_g - 20) * banhos
    print(f"Olá! Em anos de cachorro, {nome_pet} tem: {idade_real} anos. Tomou {banhos} banhos, gerando R${lucro_total} de lucro!!\n") 