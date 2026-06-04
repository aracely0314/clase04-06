contador_ing_senior=0
contador_ing_junior=0
while True:
    try:
        cantidad_ingenieros=int(input("Ingrese cantidad de ingenieros: "))
        if cantidad_ingenieros>0:
            break
        print("¡Dato inválido! Ingresa un entero positivo para continuar el registro")
    except ValueError:
        print("¡Dato inválido! Ingresa un entero positivo para continuar el registro")

for i in range(cantidad_ingenieros):
    while True:
        nombre=input("Ingrese nombre del ingeniero: ").strip()
        if len(nombre)>=6 and " " not in nombre:
            break
        print("Error! el nombre debe tener al menos 6 caracteres y no contener espacios")
    while True:
        try:
            nivel_tecnico=int(input("Ingrese mivel del ingeniero: "))
            if nivel_tecnico>0:
                break
            print("¡Error de validación! Ingresa un número entero positivo para el nivel técnico.")
        except ValueError:
            print("¡Error de validación! Ingresa un número entero positivo para el nivel técnico.")
    if nivel_tecnico>45:
        contador_ing_senior+=1
    else: 
        contador_ing_junior+=1

print(f"¡El instituto cuenta con {contador_ing_senior} Ingenieros Senior y {contador_ing_junior} Ingenieros Junior!")