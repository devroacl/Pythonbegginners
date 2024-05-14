#Escribiendo la solucion

#precios_sabores
precio_vainilla = 150
precio_chocolate = 100
precio_fresa = 160

#precios_topins
precio_choco_rallado = 20
precio_frutas = 30
precio_crema_batida = 25


# Solicitar sabor
sabor_valido = False
while not sabor_valido:
    print("Elige el sabor de helado (vainilla, chocolate, fresa):")
    sabor = input().lower()
    if sabor in ["vainilla", "chocolate", "fresa"]:
        sabor_valido = True
    else:
        print("Sabor inválido. Por favor, elige uno de los sabores disponibles.")

# Solicitar topins y calcular precio total de topins
precio_topins = 0
continuar_agregando_topins = True
while continuar_agregando_topins:
    print("¿Deseas agregar topins? (s/n):")
    respuesta = input().lower()
    if respuesta == "s":
        topin_valido = False
        while not topin_valido:
            print("Ingresa el topin:")
            topin = input().lower()
            if topin in ["chocolate rallado", "frutas", "crema batida"]:
                precio_topins += eval("precio_" + topin.replace(" ", "_"))
                topin_valido = True
            else:
                print("Topin inválido. Por favor, ingresa uno de los topins disponibles.")
    elif respuesta == "n":
        continuar_agregando_topins = False
    else:
        print("Respuesta inválida. Por favor, ingresa 's' o 'n'.")

# Calcular precio base
if sabor == "vainilla":
    precio_base = precio_vainilla
elif sabor == "chocolate":
    precio_base = precio_chocolate
else:
    precio_base = precio_fresa

# Calcular precio total
precio_total = precio_base + precio_topins

# Solicitar servicio
servicio_valido = False
while not servicio_valido:
    print("¿Para servir o para llevar? (servir/llevar):")
    servicio = input().lower()
    if servicio in ["servir", "llevar"]:
        servicio_valido = True
    else:
        print("Servicio inválido. Por favor, ingresa 'servir' o 'llevar'.")

# Aplicar descuento si es para servir
if servicio == "servir":
    precio_total -= 200

# Mostrar total a pagar
print("El total a pagar es: $" + str(precio_total))

# Solicitar pago
pago_suficiente = False
while not pago_suficiente:
    try:
        print("Ingrese el monto a pagar:")
        pago = float(input())
        if pago >= precio_total:
            pago_suficiente = True
        else:
            print("Pago insuficiente. Por favor, ingrese al menos $" + str(precio_total) + ".")
    except ValueError:
        print("Cantidad inválida. Por favor, ingrese un número válido.")

# Calcular y mostrar vuelto
vuelto = pago - precio_total
if vuelto > 0:
    print("Su vuelto es de: $" + str(vuelto))
