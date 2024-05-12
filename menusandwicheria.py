
totalRecaudado=opcPpal=0
contChoripan=contItaliano=contVegano=0
contGralChoripan=contGralItaliano=contGralVegano=0
while opcPpal != 'c':
    print("""
       Sandwichería El Duocano
    =============================
    a) Realizar Venta
    b) Cerrar Turno
    c) Salir""")
    opcPpal=input('>').lower() #transformo lectura a minúsculas
    if opcPpal.isalpha():
        if opcPpal in 'abc' and len(opcPpal)==1:
            if opcPpal == 'a':
                opcVtas=0            
                while opcVtas != 4:
                    print("""
                        Sandwich disponibles:
                    =============================
                    1.- DuocChoripan $1200
                    2.- DuocItaliano $1500
                    3.- DuocVegano $2000
                    4.- Salir """) 
                    opcVtas=0
                    while opcVtas<1 or opcVtas>4:
                        try:
                            opcVtas=int(input('>'))
                            if opcVtas<1 or opcVtas>4:     
                                print('Fuera de Rango')
                        except:
                            print('Opción es un número!!')
                    if opcVtas == 1:
                        contChoripan += 1
                    elif opcVtas == 2:
                        contItaliano += 1
                    elif opcVtas == 3:
                        contVegano += 1
                    else:
                        if contChoripan != 0:
                            contGralChoripan+=contChoripan
                            print(f'DuocChoripan {contChoripan} X $1200.....${contChoripan*1200}')
                        if contItaliano != 0:
                            contGralItaliano+=contItaliano
                            print(f'DuocItaliano {contItaliano} X $1500.....${contItaliano*1500}')
                        if contVegano != 0:
                            contGralVegano+=contVegano
                            print(f'DuocVegano {contVegano} X $2000.....${contVegano*2000}')
                        subTotal= (contChoripan*1200) + (contItaliano*1500) + (contVegano*2000)
                        print(f'Total de su cuenta: ${subTotal}')
                        totalRecaudado+=subTotal                      
                        contChoripan=contItaliano=contVegano=0     
            elif opcPpal == 'b':
                print('Resúmen Venta Diaria')
                print('='*55)
                print(f'\tCant. de DuocChoripan: {contGralChoripan}')
                print(f'\tCant. de DuocItaliano: {contGralItaliano}')
                print(f'\tCant. de DuocVegano: {contGralVegano}')
                print('='*55)
                print(f'Total Recaudado en Caja: ${totalRecaudado}')
                print('='*55)
                resp=input('¿Seguro de Cerrar la Caja? (s/n): ').upper()
                if resp == 'S':
                    contGralChoripan=contGralItaliano=contGralVegano=totalRecaudado=0
            else:
                print('Saliendo del sistema.....')
        else:
            print('Opción NO Existe!!!')
    else:
        print('Solo puede ingresar letras!!')

