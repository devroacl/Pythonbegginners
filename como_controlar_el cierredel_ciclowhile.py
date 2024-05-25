#--- En este caso se usa una variable true para abrir el ciclo

menu=True
 #--- para entendimiento "while menu" es lo mismo que "while menu== true" pero es aceptable que el codigo sea lo mas limpio y ordenado posible
while menu: #--Mientras el menu sea verdadero(true) el ciclo seguira
    #--Los Print sirven para mostrar el contenido dentro del ciclo y comprobar si se entra al ciclo
    print("Este sera el ciclo principal")
    print("Estas dentro del ciclo")
 #--AQUI VA LA PREGUNTA PARA CERRAR EL CICLO---EN CASO DE QUERER MANEJAR EL CIERRE DEL CICLO 
    salir=input('Usted desea salir del ciclo?(si/no)').lower() #-- lower() funciona para convertir la entrada del usuario en minusculas.Esto ayuda si responde NO ,nO,nO,NO,no,etc..
    if salir =='no':
        menu=True #--el menu sigue siendo verdadero(true)
    elif salir =='si':
        menu=False
        