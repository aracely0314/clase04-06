print("CALCULADORA DE DESCUENTO")
nombre=input("Ingrese su nombre:")
precio=int(input("Ingrese el precio:"))
if precio<0:
    print("ERROR! no puede ser un precio menor que 0")
porcentaje_descuento=int(input("Ingrese el porcentaje de descuento:"))
if porcentaje_descuento<0:
    print("ERROR! no puede ser un descuento menor que 0")
precio_final=precio-(precio*porcentaje_descuento/100)
