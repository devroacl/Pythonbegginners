import random as rd
import csv

def asignar_creditos(alumnos):
    creditos = {}
    for alumno in alumnos:
        creditos[alumno] = rd.randint(50, 200)
    return creditos    

def clasificar_creditos(creditos):
    menores_a_100 = {}
    entre_100_y_150 = {}
    creditos_mayores_a_150 = {}

    for alumno, credito in creditos.items():
        if credito < 100:
            menores_a_100[alumno] = credito
        elif 100 <= credito <= 150:
            entre_100_y_150[alumno] = credito
        else:
            creditos_mayores_a_150[alumno] = credito
    
    return {
        'menores a 100': menores_a_100,
        'entre 100 y 150': entre_100_y_150,
        'creditos mayores a 150': creditos_mayores_a_150
    }
    

def calcular_estadisticas(creditos):
    valores = list(creditos.values())
    maximo = max(valores)
    minimo = min(valores)
    promedio = sum(valores) / len(valores)
    
    return maximo, minimo, promedio

def generar_csv(creditos, clasificacion, filename='archivocsv.csv'):
    try:
        with open(filename, 'w', newline='',encoding='utf-8') as csvfile:
            fieldnames = ['Nombre', 'Creditos', 'Clasificacion']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for alumno, credito in creditos.items():
                if credito < 100:
                    clasif = 'menores a 100'
                elif 100 <= credito <= 150:
                    clasif = 'entre 100 y 150'
                else:
                    clasif = 'mayores a 150'
                    
                writer.writerow({'Nombre': alumno, 'Creditos': credito, 'Clasificacion': clasif})
    except Exception as e:
        print(f'Error al guardar archivo: {e}')
