import os, time
print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
menu_principal="""===MENÚ PRINCIPAL===
1. Habitaciones disponibles
2. Realizar check-in
3. Realizar check-out
4. Historial de ocupaciones
5. Salir"""
habitaciones_disponibles=50
while True:
    os.system("cls")
    print(menu_principal)
    opcion=input("Ingrese la opción que desea (1-5): ")
    os.system("cls")
    if opcion=="1":
        print("HABITACIONES DISPONIBLES")
        print(f"Cantidad de habitaciones disponibles en el hotel: {habitaciones_disponibles}")
        print("Volviendo al menú principal...")
        time.sleep(2)
    elif opcion=="2":
        pass
    elif opcion=="3":
        pass
    elif opcion=="4":
        pass
    elif opcion=="5":
        print("¡Gracias por usar el sistema de gestión de habitaciones del Hotel Estelar! ¡Hasta luego!")
        time.sleep(2)
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida (1-5).")
        time.sleep(2)
    time.sleep(2)