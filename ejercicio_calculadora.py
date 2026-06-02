print("CALCULADORA DE DESCUENTO")
while True:
    nombre=input("Ingrese su nombre:")
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
        if porcentaje_descuento<0:
            print("ERROR! no puede ser un descuento menor que 0")
        else:
            break
    except ValueError:
        print("Error! el descuento debe ser números válidos")
precio_final=precio-(precio*porcentaje_descuento/100)
