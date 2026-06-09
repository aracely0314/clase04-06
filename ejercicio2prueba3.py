import os, time
print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
menu_principal="""===MENÚ PRINCIPAL===
1. Habitaciones disponibles
2. Realizar check-in
3. Realizar check-out
4. Historial de ocupaciones
5. Salir"""
habitaciones_disponibles=50
reservar_habitacion=0
habitaciones_disponibles=50
total_reservas=0
cancelar_habitacion=0
habitaciones_en_reserva=0
total_habitaciones_reservadas=0
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
        print("REALIZAR CHECK-IN")
        while True:
            if habitaciones_disponibles==0:
                print("No hay habitaciones disponibles")
                print("Volviendo al menú principal...")
                time.sleep(1.3)
                break
            try:
                reservar_habitacion=int(input("Ingrese cantidad de habitaciones que desea reservar:"))
                if reservar_habitacion>0 and reservar_habitacion<=habitaciones_disponibles:
                    print(f"{reservar_habitacion} habitaciones reservadas con éxito!")
                    habitaciones_disponibles-=reservar_habitacion
                    habitaciones_en_reserva+=reservar_habitacion
                    total_reservas+=1
                    total_habitaciones_reservadas+=reservar_habitacion
                    print("Volviendo al menú principal...")
                    time.sleep(1.5)
                    break
                elif reservar_habitacion>habitaciones_disponibles:
                    print("Cantidad de habitaciones que desea reservar supera la cantidad de habitaciones disponibles.")
                    continue
                print ("Error! Debe ingresar un número entero positivo válido")
            except ValueError:
                print("Error! Debe ingresar un número entero positivo válido")
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