contador_ing_senior=0
contador_ing_junior=0
cantidad_ingenieros=int(input("Ingrese cantidad de ingenieros: "))

for i in range(cantidad_ingenieros):
    nombre=input("Ingrese nombre del ingeniero: ")
    nivel_tecnico=int(input("Ingrese mivel del ingeniero: "))
    if nivel_tecnico>45:
        contador_ing_senior+=1
    else: 
        contador_ing_junior+=1

print(f"¡El instituto cuenta con {contador_ing_senior} Ingenieros Senior y {contador_ing_junior} Ingenieros Junior!")