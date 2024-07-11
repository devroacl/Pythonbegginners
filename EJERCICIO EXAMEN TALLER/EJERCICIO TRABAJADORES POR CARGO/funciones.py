import random as rd
import csv

# Función para asignar sueldos aleatorios a los trabajadores
def asignar_sueldos(trabajadores, cargos):
    sueldos = {}
    for trabajador, cargo in zip(trabajadores, cargos):
        sueldos[trabajador] = {
            "sueldo_bruto": rd.randint(100000, 900000),
            "cargo": cargo
        }
    return sueldos


# Función para calcular descuentos y sueldo líquido
def calcular_sueldo_liquido(sueldo_bruto):
    descuento_afp = sueldo_bruto * 0.10
    descuento_salud = sueldo_bruto * 0.07
    sueldo_liquido = sueldo_bruto - descuento_afp - descuento_salud
    return {
        "sueldo_bruto": sueldo_bruto,
        "descuento_afp": round(descuento_afp) ,
        "descuento_salud":round(descuento_salud)  ,
        "sueldo_liquido": round(sueldo_liquido)  
    }

# Función para calcular estadísticas de sueldos
def calcular_estadisticas(sueldos):
    if not sueldos:
        return None, None, None
    valores = [datos["sueldo_bruto"] for datos in sueldos.values()]
    maximo = max(valores)
    minimo = min(valores)
    promedio = sum(valores) / len(valores)
    return maximo, minimo, promedio


# Función para guardar el reporte en CSV
def guardar_csv(sueldos, filename='reporte_sueldos.csv'):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as filecsv:
            fieldnames = ['Nombre', 'Cargo', 'Sueldo Bruto', 'Descuento AFP', 'Descuento Salud', 'Sueldo Líquido']
            writer = csv.DictWriter(filecsv, fieldnames=fieldnames)
            writer.writeheader()
            for trabajador, datos in sueldos.items():
                datos_sueldo = calcular_sueldo_liquido(datos["sueldo_bruto"])
                writer.writerow({
                    'Nombre': trabajador,
                    'Cargo': datos["cargo"],
                    'Sueldo Bruto': datos_sueldo["sueldo_bruto"],
                    'Descuento AFP': datos_sueldo["descuento_afp"],
                    'Descuento Salud': datos_sueldo["descuento_salud"],
                    'Sueldo Líquido': datos_sueldo["sueldo_liquido"]
                })
    except Exception as e:
        print(f'Error en el guardado: {e}')


# Función para guardar el reporte en CSV por cargo
def guardar_csv_por_cargo(sueldos, cargo, filename=None):
    if filename is None:
        filename = f'reporte_sueldos_{cargo}.csv'
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as filecsv:
            fieldnames = ['Nombre', 'Cargo', 'Sueldo Bruto', 'Descuento AFP', 'Descuento Salud', 'Sueldo Líquido']
            writer = csv.DictWriter(filecsv, fieldnames=fieldnames)
            writer.writeheader()
            for trabajador, datos in sueldos.items():
                if datos["cargo"] == cargo:
                    datos_sueldo = calcular_sueldo_liquido(datos["sueldo_bruto"])
                    writer.writerow({
                        'Nombre': trabajador,
                        'Cargo': datos["cargo"],
                        'Sueldo Bruto': datos_sueldo["sueldo_bruto"],
                        'Descuento AFP': datos_sueldo["descuento_afp"],
                        'Descuento Salud': datos_sueldo["descuento_salud"],
                        'Sueldo Líquido': datos_sueldo["sueldo_liquido"]
                    })
    except Exception as e:
        print(f'Error en el guardado: {e}')
