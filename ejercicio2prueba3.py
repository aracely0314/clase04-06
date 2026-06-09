import os,time
menu_principal= """*** MENU PRINCIPAL ***
1.- Cupos disponibles.
2.- Realizar reserva.
3.- Cancelar reserva.
4.- Historial de reservas.
5.- Salir."""
cupos_disponibles=75
reservar_cupos=0
total_reservas=0
cancelar_cupos=0
cupos_en_reserva=0
total_cupos_reservados=0
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
        print("RESERVAR CUPOS")
        while True:
            if cupos_disponibles==0:
                print("No hay cupos disponibles")
                print("Volviendo al menú principal...")
                time.sleep(1.3)
                break
            try:
                reservar_cupos=int(input("Ingrese cantidad de cupos que desea reservar:"))
                if reservar_cupos>0 and reservar_cupos<=cupos_disponibles:
                    print(f"{reservar_cupos} cupos reservados con éxito!")
                    cupos_disponibles-=reservar_cupos
                    cupos_en_reserva+=reservar_cupos
                    total_reservas+=1
                    total_cupos_reservados+=reservar_cupos
                    print("Volviendo al menú principal...")
                    time.sleep(1.5)
                    break
                elif reservar_cupos>cupos_disponibles:
                    print("Cantidad de cupos que desea reservar supera la cantidad de cupos disponibles.")
                    continue
                print ("Error! Debe ingresar un número entero positivo válido")
            except ValueError:
                print("Error! Debe ingresar un número entero positivo válido")
    elif opcion=="3":
        print("CANCELAR RESERVA DE CUPOS")
        while True:
            if cupos_en_reserva==0:
                print("No hay cupos reservados para cancelar")
                print("Volviendo al menú principal...")
                time.sleep(1)
                break
            try:
                cancelar_cupos=int(input("Ingrese cantidad de cupos que desea cancelar: "))
                if cancelar_cupos>=0 and cancelar_cupos<=cupos_en_reserva and cancelar_cupos<=75:
                    cupos_disponibles+=cancelar_cupos
                    cupos_en_reserva-=cancelar_cupos
                    print("Se ha cancelado la reserva de cupo con éxito")
                    print("Volviendo al menú principal...")
                    time.sleep(1.5)
                    break
                else: 
                    if cancelar_cupos>75 and cancelar_cupos>cupos_en_reserva:
                        print("Error! El número ingresado es mayor a la capacidad máxima del gimnasio o supera el número de cupos en reserva")
                    else:
                        print("Error! Debe ingresar un número entero válido mayor o igual a 0")
            except ValueError:
                print("Error! Debe ingresar un número entero válido mayor o igual a 0")
    elif opcion=="4":
        pass
    elif opcion=="5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        time.sleep(2)
        break
    else:
        print("Error! Opcion no válida, debe ingresar una opción entre 1 y 5")
    time.sleep(2)
