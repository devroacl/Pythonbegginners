productos =["lentejas","arroz","papas","aceite","mayonesa","carne"]

precios=[1000,2000,5000,5000,4000,5000]

#----ZIP SE USA PARA COMBINAR AMBAS LISTAS ... SE PUEDE HACER EN LISTAS Y TUPLAS
#---es para solo hacer el menu de Agregar productos
menutotal= list(zip(productos,precios))

carrito=[]
#---Las elecciones en el menu de productos se guardaran como Int en el carrito 
# y luego se accederan a ellas con ciclos for.

total=0

contadornum=1 

#--DECIDI INICIAR COMO STR PORQUE CON INT NO ME FUNCIONABA EL CODIGO del menu
opcion=0

continuar=True
  #ESTO ES PARA EL MENU DE PRINCIPAL---  
   
print("---"*10)    
print(' SUPERMERCADO')
print("---"*10)


while continuar:
    print("""
        1)	Agregar productos
        2)	Ver canasta
        3)Ver total
        4) Salir
        """)
    opcion=0
    while opcion<1 or opcion>4:
        try:
            #---esto hace que hasta que vuelva a pedir elegir una opcion hasta que esta sea valida 
            opcion=int(input("Elige una opcion --> "))
            
            if opcion< 1 or opcion>4:
                print("opcion no existe")
        except:
            print("opcion debe ser un numero del menu") 
            
#---Aqui entran las opciones del menu una vez dada una opcion valida       
    
    if opcion==1:
        #ESTO ES PARA EL MENU DE PRODUCTOS----   
        print("---"*10)    
        print('  menu supermercado')
        print("---"*10)
        contadornum=1
        #---no te olvides de agregar el contador antes de iniciar el ciclo. 
        for ingrediente,valor in menutotal:
            print(f"{contadornum} {ingrediente}-{valor}")
            contadornum=contadornum+1

        print("---"*10)    
        print('  Elije una opcion--> ')
        print("---"*10)
                                    
        #-----------------  AQUI DEBE HABER UNA FORMA DE SACAR LA LISTA AUN SI SE MODIFICA ARRIBA 
        
        producto_valido=False
        #--inicializado en falso para poder ponerlo en un while not que convierte el falso en verdadero
        #PARA NO USAR BREAK  
        
        
        while not producto_valido:
            try:
                comprar= int(input('---->'))
                if comprar>=1 and comprar<=len(productos):
                    #---LEN(PRODUCTOS)ES PARA QUE LA OPCION ESTE DENTRO DEL RANGO DE LA LISTA EN ESTE CASO PRODUCTOS.
                    #---comprar -1 es para restarle 1 a la opcion del usuario 
                    # ya que los indices de listas comienzan en 0 1 2 3   Si el usuario elije 1 estaria eligiendo el indice 0 
                    # y asi consecutivamente
                    carrito.append(comprar-1)
                    #--carrito.append es para agregarlo a la lista carro en la opcion 2
                    print(f'{productos[comprar-1]}  agregado al carrito')
                    producto_valido=True
                    #---convierte el producto valido en true y cuando llegue el siguiente bucle producto_valido sera falso ya que "# while not True -> while False (el bucle no se ejecuta y termina"
                else:
                    print('producto no existe')
                
            except:
                print('numero u opcion no valida')
        
        
    elif opcion==2:
        print('ver canasta')
        if len(carrito)== 0:
            print('esta vacio')
           #----- if carrito == []: o if len(carrito) == 0: OTRAS FORMAS DE HACERLO if not carrito:
            
        else:
            print("---"*10) 
            print("Productos en el carrito:")
            print("---"*10) 
            #--
            print("---"*10) 
            for producto_i in carrito:
                print(f"{productos[producto_i]} - $ {precios[producto_i]}") 
                    
                #----EJEMPLO PARAENTENDER En este caso, carrito contiene los índices [2, 4], lo que significa que el usuario 
                # ha seleccionado , "papas" y "mayonesa".
                # #----Al ejecutar el bucle for, esto es lo que ocurre:
                #Primera Iteración:
                    #producto_i = 2
                    #productos[2] es "papas"
                    #precios[2] es 5000
                    #Se imprime: papas - $5000
                    
                    #segunda Iteración:

                    #producto_i = 4
                    #productos[4] es "mayonesa"
                    #precios[4] es 4000
                    #Se imprime: mayonesa - $4000
            print("---"*10)         
        total=0 
    elif opcion==3:
        print('ver total')
        if len(carrito)== 0:
            print("---"*10) 
            print('Carrito vacio,Agregue Productos')
            print("---"*10) 
        else:
            print("---"*10) 
            for producto_i in carrito:
                total=total+precios[producto_i]
            #----total=sum(precios[producto_i] for producto_i in carrito) una forma de hacerlo pero un poco mas avanzado para mi
            print(f" Total a pagar  {total}")
            print("---"*10) 
        
    elif opcion==4:
        continuar=False
        print('Ha elegido  salir')
        print('vuelva pronto')
        
