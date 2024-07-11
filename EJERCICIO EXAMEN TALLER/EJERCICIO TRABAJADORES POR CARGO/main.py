from funciones import *

def menu():
    trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
                    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
                    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
    
    cargos = ["CEO", "DESARROLLADOR", "ANALISTA DE DATOS", "DESARROLLADOR", 
            "ANALISTA DE DATOS", "CEO", "DESARROLLADOR", 
            "ANALISTA DE DATOS", "CEO", "DESARROLLADOR"]
    
    sueldos = {}
    
    while True:
        print('**' * 15)
        print('Gestión de Sueldos para Trabajadores')
        print('**' * 15)
        print('\n1 - Asignar sueldos')
        print('2 - Calcular estadísticas de sueldos')
        print('3 - Generar reporte de sueldos')
        print('4 - Generar reporte de sueldos por cargo')
        print('5 - Salir')
        print()
        
        opcion = 0
        try:
            opcion = int(input('Ingresa una opción válida --> '))
            if opcion < 1 or opcion > 5:
                print('Opción fuera de rango')
        except:
            print('Opción no válida')
        
        if opcion == 1:
            sueldos = asignar_sueldos(trabajadores, cargos)
            print('¡Se han asignado los sueldos a los trabajadores!')
            for trabajador, datos in sueldos.items():
                print(f'{trabajador} ({datos["cargo"]}): ${datos["sueldo_bruto"]}')
        elif opcion == 2:
            maximo, minimo, promedio = calcular_estadisticas(sueldos)
            print(f'Sueldo máximo: ${maximo}')
            print(f'Sueldo mínimo: ${minimo}')
            print(f'Sueldo promedio: ${promedio}')
        elif opcion == 3:
            guardar_csv(sueldos)
            print('Reporte guardado exitosamente')
        elif opcion == 4:
            cargo = input('Ingrese el cargo para el reporte (CEO, Desarrollador, Analista de Datos): ').upper()
            if cargo in cargos:
                guardar_csv_por_cargo(sueldos, cargo)
                print(f'Reporte de sueldos para {cargo} guardado exitosamente')
            else:
                print('Cargo no válido')
        elif opcion == 5:
            break

if __name__ == "__main__":
    menu()
