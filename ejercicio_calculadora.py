print("CALCULADORA DE DESCUENTO")
while True:
    nombre=input("Ingrese nombre del producto:")
    if not nombre.isnumeric():
        break
    else:
        print("Error! el nombre no pueden ser números")
while True:
    try:
        precio=int(input("Ingrese el precio:"))
        if precio<0:
            print("ERROR! no puede ser un precio menor que 0")
        else: 
            break
    except ValueError:
        print("Error! el precio debe ser números válidos")
while True:
    try:
        porcentaje_descuento=int(input("Ingrese el porcentaje de descuento:"))
        if porcentaje_descuento<0 and porcentaje_descuento>100:
            print("ERROR! no puede ser un descuento menor que 0 ni mayor a 100")
        else:
            break
    except ValueError:
        print("Error! el descuento debe ser números válidos")
precio_final=precio-(precio*porcentaje_descuento/100)

print(f""" Producto: {nombre}
Precio original: {precio}
Descuento: {descuento}%
Precio Final: {int(precio_final)}""")
