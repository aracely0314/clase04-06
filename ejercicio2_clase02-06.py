print("PROMEDIO NOTAS")
while True:
    try:
        cantidad_notas = int(input("Cuántas notas deseas ingresar?: "))
        if cantidad_notas <= 0:
            print("La cantidad de notas debe ser mayor a cero.")
        else:
            break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero válido.")

suma_notas = 0
for i in range(cantidad_notas):
    while True:
        try:
            nota=float(input(f"Ingrese nota {i+1}: "))
            if nota<0 or nota>10:
                print("La nota debe ser mayor que 0 y menor o igual que 7.0")
            else:
                suma_notas += nota
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número decimal válido.")

promedio = suma_notas / cantidad_notas
if promedio>= 4.0:
    estado= "Aprobado"
else:
    estado= "Reprobado"
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}")
