saldo=100000
menu="""MENÚ:
1. Consultar saldo
2. Depositar dinero
3. Girar dinero
4. Salir"""
while True:
    print(menu)
    opcion=input("Seleccione una opción (1-4): ")
    if opcion=="1":
        print(f"Saldo actual: ${saldo}")
    elif opcion=="2":
        while True:
                deposito=int(input("Monto a depositar: "))
                break
    elif opcion=="3":
        while True:
                giro=int(input("Monto a girar: "))
                break
    elif opcion=="4":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break