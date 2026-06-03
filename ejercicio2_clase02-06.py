print("PROMEDIO NOTAS")
cantidad_notas = int(input("Cuántas notas deseas ingresar?: "))
if cantidad_notas <= 0:
    print("La cantidad de notas debe ser mayor a cero.")
for i in range(cantidad_notas):
    nota=float(input(f"Ingrese nota {i+1}: "))
    if nota<0 or nota>10:
        print("La nota debe ser mayor que 0 y menor o igual que 7.0")
    else:
       suma_notas += nota

promedio = suma_notas / cantidad_notas