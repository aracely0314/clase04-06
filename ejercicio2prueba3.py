import os,time
menu_principal= """*** MENU PRINCIPAL ***
1.- Cupos disponibles.
2.- Realizar reserva.
3.- Cancelar reserva.
4.- Historial de reservas.
5.- Salir."""
cupos_disponibles=75
print("¡Bienvenido al sistema de gestión de cupos del Gimnasio Titan!")
while True:
    os.system("cls")
    print(menu_principal)
    opcion=input("Ingrese la opción que desea (1-5): ")
    os.system("cls")
    if opcion=="1":
        print("Cupos disponibles")
        print(f"Cantidad de cupos disponibles en el gimnasio: {cupos_disponibles}")
        print("Volviendo al menú principal...")
        time.sleep(2)
    elif opcion=="2":
       pass
    elif opcion=="3":
        pass
    elif opcion=="4":
        pass
    elif opcion=="5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        time.sleep(2)
        break
    else:
        print("Error! Opcion no válida, debe ingresar una opción entre 1 y 5")
    time.sleep(2)
