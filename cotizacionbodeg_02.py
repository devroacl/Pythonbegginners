print("===Bodegas 'La Bodeguita'===")
flag=True
precio_bodega=250000
capacidad=35
largo=ancho=alto=cantidad=0
print('Ingrese medidas en cms: ')
while largo<=0:
    try:        
        largo=int(input('Largo: '))        
        if largo <= 0:
            print('debe ser MAYOR a CERO')
    except:
        print('Debe ser nº') 

while ancho<=0:
    try:        
        ancho=int(input('Ancho: '))        
        if ancho <= 0:
            print('debe ser MAYOR a CERO')
    except:
        print('Debe ser nº') 

while alto<=0:
    try:        
        alto=int(input('Alto: '))       
        if alto <= 0:
            print('debe ser MAYOR a CERO')
    except:
        print('Debe ser nº')

while cantidad<=0:
    try:        
        cantidad=int(input('Ingrese la cantidad de cajas: '))       
        if cantidad <= 0:
            print('debe ser MAYOR a CERO')
    except:
        print('Debe ser nº')


caja_m3=(largo/100)*(ancho/100)*(alto/100)
total_m3=caja_m3*cantidad
bodega=1
while total_m3 > (capacidad*bodega):
    bodega+=1

print(f'Los m3 de todas las cajas es {total_m3}m3')
print(f'Necesita {round(bodega,2)} bodegas')
print(f'El costo total por arriendo será ${bodega*precio_bodega}')
