# Saldo inicial en cuenta
saldo = 100000
# Loop principal del programa
flag = True
while flag:
    # Mostrar menú
    print("Bienvenido al Banco del País, seleccione una opción")
    print("1. Consultar Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")
    # Solicitar opción al usuario
    opcion = input("Selecciona una opción (1-3):")
    # Realizar acciones según la opción seleccionada
    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo}")
    elif opcion == "2":
        retiro = 0
        while retiro <= 0: #ciclo de validación, se repite mientras ingreso es NO válido
            try:
                retiro = int(input('Ingrese monto a retirar: $'))
                if retiro <= 0:
                    print('Debe ser MAYOR a CERO')
            except:
                print('Solo se admiten números!!!')
        if retiro <= saldo:
            saldo -= retiro
            print(f'Se hace retiro de ${retiro} y su nuevo saldo es ${saldo}')
        else:
            print('No tiene saldo suficiente!!')
    elif opcion == "3":
        print("Gracias por utilizar el Cajero.")
        flag = False
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
