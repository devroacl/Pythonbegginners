from funciones import *

def menu():

    alumnos = ["Juan Pérez", "María García", "Carlos López", 
           "Ana Martínez", "Pedro","Rodríguez", "Laura Hernández", 
           "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"] 
    #INICIAR EL MENU PRINCIPAL CON OPCIONES 
    #PONER UN TRY Y EXCEPT 
    
    creditos={}
    clasificacion={}
    
    menuprincipal=True
    while menuprincipal: 
        print('Asignacion de creditos')
        print('1-')
        print('2-')
        print('3-o')
        print('4-Salir del programa')
        opcion=0
        try:
            opcion=int(input('Ingrese opcion valida---> '))
            if opcion<1 or opcion>4:
                print('Opcion fuera de rango')
        except:
            print('Opcion no valida intente de nuevo')       
            
        if opcion==1:
            print('invocar funcion 1')
            creditos=asignar_creditos(alumnos)
            print("Créditos asignados correctamente.")
        elif opcion==2:
            print('invocar funcion op2')
            clasificacion = clasificar_creditos(creditos)
            for categoria, estudiantes in clasificacion.items():
                    print(f"\n{categoria.title()}:")
                    for alumno, credito in estudiantes.items():
                        print(f"{alumno}: ${credito}")
        elif opcion==3:
            print('invocar funcion op2')
            maximo, minimo, promedio = calcular_estadisticas(creditos)
            print(f"Máximo Crédito: ${maximo}")
            print(f"Mínimo Crédito: ${minimo}")
            print(f"Promedio de Créditos: ${promedio:.2f}")
        elif opcion==4: 
            generar_csv(creditos, clasificacion)
            print("Reporte CSV generado correctamente.")

        elif opcion==5:
            print('saliendo del programa')
            menuprincipal=False  
        
    #INICIAR EL MENU PRINCIPAL CON OPCIONES 
    #PONER UN TRY Y EXCEPT 
if __name__ == "__main__":
    menu() 