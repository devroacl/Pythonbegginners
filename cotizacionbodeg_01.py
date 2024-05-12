print("===Bodegas 'La Bodeguita'===")
flag=True
precio_bodega=250000
capacidad=35
while flag:
    try:
        print('Ingrese medidas en cms: ')
        largo=int(input('Largo: '))
        ancho=int(input('Ancho: '))
        alto=int(input('Alto: '))
        cantidad=int(input('Ingrese la cantidad de cajas: '))
        if largo>0 and ancho>0 and alto>0 and cantidad>0:
            flag=False
        else:
            print('deben ser MAYOR a CERO')
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
