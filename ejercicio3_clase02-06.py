import os, time
saldo=100000
menu="""MENÚ:
1. Consultar saldo
2. Depositar dinero
3. Girar dinero
4. Salir"""
while True:
    os.system("cls")
    print(menu)
    opcion=input("Seleccione una opción (1-4): ")
    if opcion=="1":
        print(f"Saldo actual: ${saldo}")
    elif opcion=="2":
        while True:
            try:
                deposito=int(input("Monto a depositar: "))
                if deposito<0:
                    print("El monto a depositar debe ser mayor o igual a cero.")
                else:
                    saldo+=deposito
                    print(f"Depósito realizado")
                    time.sleep(1)
                    break
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero válido.")
    elif opcion=="3":
        while True:
            try:
                giro=int(input("Monto a girar: "))
                if giro>saldo:
                    print("No tiene suficiente saldo para realizar el giro, ingrese monto dentro del saldo.")
                else:
                    saldo-=giro
                    print(f"Giro realizado")
                    time.sleep(1)
                    break
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero válido.")
    elif opcion=="4":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        time.sleep(2)
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        time.sleep(2)