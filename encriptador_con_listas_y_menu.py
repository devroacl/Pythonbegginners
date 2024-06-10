import csv

listaCenit = ['C', 'E', 'N', 'I', 'T']
listaPolar = ['P', 'O', 'L', 'A', 'R']

# Lista para almacenar las palabras encriptadas y desencriptadas
palabrasGuardadas = []
continuar = True

palabraEncriptada=[]
palabraDesencriptada=[]

while continuar:
    print("""
        1) Encriptar
        2) Desencriptar
        3) Salir
    """)
    
    
    opcion = 0

    while opcion < 1 or opcion > 3:
        try:
            opcion = int(input('>'))
            if opcion < 1 or opcion > 3:
                print("Opcion no existe")
        except ValueError:
            print('Elige una opcion valida del menu')

    if opcion == 1:
        print('Vamos a encriptar un texto')
        palabra = input('Ingrese palabra: ').upper()
        palabraEncriptada = []

        # Recorre cada letra de la palabra ingresada
        for letra in palabra:
            if letra in listaCenit:
                i = listaCenit.index(letra)
                nueva_letra = listaPolar[i]
                palabraEncriptada.append(nueva_letra)
            elif letra in listaPolar:
                i = listaPolar.index(letra)
                nueva_letra = listaCenit[i]
                palabraEncriptada.append(nueva_letra)
            else:
                palabraEncriptada.append(letra)
        
        palabraEncriptada_str = ''.join(palabraEncriptada)
        
        palabrasGuardadas.append({
            'Palabra Encriptada': palabraEncriptada_str,
            'Palabra Desencriptada': palabra
        })

        print("Palabra encriptada:", palabraEncriptada_str)

    elif opcion == 2:
        print('Vamos a desencriptar')
        palabras_desencriptadas = False  # Bandera para verificar si hay palabras desencriptadas

        try:
            with open('EncriptadorCSV.csv', 'r', newline='') as archivoCSV:
                lectorCSV = csv.DictReader(archivoCSV)
                for fila in lectorCSV:
                    palabraEncriptada = fila['Palabra Encriptada']
                    palabraDesencriptada = []

                    for letra in palabraEncriptada:
                        if letra in listaPolar:
                            i = listaPolar.index(letra)
                            nueva_letra = listaCenit[i]
                            palabraDesencriptada.append(nueva_letra)
                        elif letra in listaCenit:
                            i = listaCenit.index(letra)
                            nueva_letra = listaPolar[i]
                            palabraDesencriptada.append(nueva_letra)
                        else:
                            palabraDesencriptada.append(letra)

                    palabraDesencriptada_str = ''.join(palabraDesencriptada)
                    print(f'Palabra Encriptada: {palabraEncriptada}, Palabra Desencriptada: {palabraDesencriptada_str}')
                    palabras_desencriptadas = True

            if not palabras_desencriptadas:
                print('No hay palabras encriptadas en el archivo.')

        except FileNotFoundError:
            print('Error: El archivo no existe.')

    elif opcion == 3:
        print('Guardando las palabras en un archivo CSV y saliendo del programa...')
        with open('EncriptadorCSV.csv', 'w', newline='') as archivoCSV:
            miFila = csv.DictWriter(archivoCSV, fieldnames=['Palabra Encriptada', 'Palabra Desencriptada'])
            miFila.writeheader()
            miFila.writerows(palabrasGuardadas)

        if continuar:
                resp = input('¿Quieres seguir encriptando o desencriptando? (yes/no): ').lower()
                if resp != 'yes':
                    continuar = False
