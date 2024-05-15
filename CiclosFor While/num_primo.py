#CicloFor

'''
Ejercicio 3:
Ingrese un número entero mayor a cero por teclado e indique si es o no
“Primo”.
'''
num=int(input('Ingrese un número: '))
if num>0:
    esPrimo=True
    for x in range(2,num):
        if num%x==0:
            esPrimo=False
    #fuera del ciclo veo si cambió el lógico
    if esPrimo:
        print(num,'es PRIMO')
    else:
        print(num,'NO es PRIMO')
else:
    print('Debe ser un número Mayor a CERO ')
