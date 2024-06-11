import csv

listaCenit =['C', 'E', 'N', 'I', 'T']
listaPolar =['P', 'O', 'L', 'A', 'R']

#--Aqui se guardara la palabra encriptada
palabraEncriptada=[]

#---Aqui se guardaran todas las palabras 
palabrasGuardadas=[]

continuar=True
opcion=0

while continuar:
    print("""
        1)	Encriptar
        2)	Desencriptar
        3)  Salir 
       """ ) #3ra opcion se guarda el archivo csv etc etc comoarchivo csv
    #Y luego de guardarse se puede salir del ciclo. 
    
    opcion=0
    
    while opcion<1 or opcion>3:
        try:
            opcion=int(input('>'))
            
            if opcion<1 or opcion>3:
                print("Opcion no existe")
        except ValueError:
            print('elige una opcion valida del menu')
     #Imprimir opciones menu 
                
    if opcion==1:
                                #----LOGICA PARA ENCRIPTAR--------
        palabra = input('Ingrese palabra').upper()
        palabraEncriptada=[]
        #--Recorre cada letra de la palabra ingresada con un ciclo for.El upper es porque las listas cenit y polar tienen en sus indices Mayusculas.
        for letra in palabra:
            if letra in listaCenit:
                i= listaCenit.index(letra)
                nueva_letra=listaPolar[i]
                palabraEncriptada.append(nueva_letra)
                                        
            elif letra in listaPolar:
                i= listaPolar.index(letra)
                nueva_letra=listaCenit[i]
                palabraEncriptada.append(nueva_letra)
            else:
                palabraEncriptada.append(letra)
        palabraEncriptada_string = ''.join(palabraEncriptada)
        
        #--Se guarda la palabra encriptada en la lista palabra encriptada pero la palabra ya concatenada
        palabraEncriptada.append(palabraEncriptada_string)
        #---Se guardan las palabras Encriptadas y desencriptadas en lalista palabras Guardadas en formato diccionario
        palabrasGuardadas.append({
                                                'Palabra Encriptada': palabraEncriptada_string,
                                                'Palabra Desencriptada': palabra
                                            })          
        print("Palabra encriptada:", palabraEncriptada_string)   #--IMPRIME LA PALABRA encriptada ya concantenada.         
                  
          #--SI ingresas una palabra nueva en la opcion 1 y luego eliges opcion 2 (desencriptar) la palabra no aparece porque
          #--No las haz guardado y tienes que ir a la opcion 3 y salir. El programa no guarda automaticamente la informacion.Debes ir a op 3 para actualizar.                                  
    elif opcion==2:
        print('Si no aparece informacion es que el archivo esta vacio')
        try:
         with open('EncriptadorCSV.csv', 'r', newline='') as archivoCSV:
            lectorCSV = csv.DictReader(archivoCSV)
            for fila in lectorCSV:
                palabraEncriptada = fila['Palabra Encriptada']
                palabraDesencriptada = []
                #--AQUI PERMITE VER  EL ARCHIVO CSV EN FILAS Y COLUMNAS.
                #--SOLO IMPRIME INFORMACION QUE ESTA GUARDADA Y ACTUALIZADA
                for letra in palabraEncriptada:
                    if letra in listaCenit:
                        i = listaCenit.index(letra)
                        nueva_letra = listaPolar[i]
                        palabraDesencriptada.append(nueva_letra)
                    elif letra in listaPolar:
                        i = listaPolar.index(letra)
                        nueva_letra = listaCenit[i]
                        palabraDesencriptada.append(nueva_letra)
                    else:
                        palabraDesencriptada.append(letra)
                palabraDesencriptada_string = ''.join(palabraDesencriptada)
                print(f'Palabra Encriptada: {palabraEncriptada}, Palabra Desencriptada: {palabraDesencriptada_string}')
        except FileNotFoundError:
            print('Error: El archivo')
            
        #--ESTO ES PARA IMPRIMIR UNA SOLA COLUMNA PERO NO ME DEJA ENTRAR AL MENU PRINCIPAL CON ESTO...
        """  
        try:
        with open('EncriptadorCSV.csv', 'r', newline='') as archivoCSV:
            lectorCSV = csv.DictReader(archivoCSV)
            for fila in lectorCSV:
                palabraEncriptada = fila['Palabra Encriptada']
                palabraDesencriptada = fila['Palabra Desencriptada']
                print(f'Palabra Encriptada: {palabraEncriptada}, Palabra Desencriptada: {palabraDesencriptada}')
                #---   Se imprime las palabras encriptadas y desencriptadas. 
        except FileNotFoundError: #--En caso de que se ingrese por primera vez no agarre error.
                print('Error: El archivo no existe.')"""
            
    elif opcion==3:
       #-- print('aqui se sale del menu y se guarda el archivo.') 
        resp=input('Estas seguro que quieres salir? (yes/no)').lower()
        if resp=='yes':
            print(5*'--')
            print('Esta eligiendo la Opcion3 que guardara las palabras en un archivo csv')
            print(5*'--')
            #---AQUI SE GUARDA EL ARCHIVO. 
        with open('EncriptadorCSV.csv', 'w', newline='') as archivoCSV:
                miFila = csv.writer(archivoCSV)
                miFila.writerow(['Palabra Encriptada', 'Palabra Desencriptada'])
                for palabra in palabrasGuardadas:
                    miFila.writerow([palabra['Palabra Encriptada'], palabra['Palabra Desencriptada']])
        continuar=False
        
#---Cuando guardamos informacion en el csv solo se guarda la interaccion con el menu.y si hubo informacion en el csv se borra y 
#--y se actualiza con la nueva actualizacion.    
