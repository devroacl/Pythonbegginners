flag=True
opcion=0

while flag:
     print("""
            1.encender/apagar luces patio (Alternado)
            2.encender/apagar luces sala (Alternado)
            3.encender/apagar luces pasillo (Alternado)
            4.encender/apagar luces Jardin (Alternado)
            5.encender todo (Alternado)
            6.apagar todo (Alternado)
            7.salir del sistema (Alternado)""")
     try:
         opcion=int(input('ingrese opcion deseada'))
     except:
         print('ingresa solo numeros validos')
         continue     #Es para volver al inicio del ciclo.Es algo que aprendi investigando para el codigo.
      #El `continue` se utiliza en este caso para volver al inicio del bucle `while` después de manejar la excepción. Cuando el usuario ingresa una letra en lugar de un número y se genera una excepción `ValueError`, el programa muestra un mensaje de error y ejecuta la instrucción continue.
      # Esto hace que el flujo del programa vuelva al inicio del bucle `while`,
      # donde se solicita nuevamente al usuario que ingrese una opción. Sin el `continue`, el programa simplemente se detendría después de manejar la excepción y no volvería a solicitar la entrada al usuario, lo que no sería deseable en este caso.
    
     if opcion ==1:
        print('el patio esta encendido')
     elif opcion ==2:
         print('La sala esta encendida')
     elif opcion==3:
         print('el pasillo esta encendido')
     elif opcion==4:
         print('el jardin esta encendido')
     elif opcion==5:
         print('encender todo')
     elif opcion==6:
         print('Apagar todo')
     elif opcion==7:
         print('usted esta saliendo del sistema')
         flag=False #Anotacion personal.Por fin logre entender como usar la bandera.Siempre se me quedaba el ciclo en infinito y no paraba JAJAJAJA
     else:
         print('ingresa numeros validos')
