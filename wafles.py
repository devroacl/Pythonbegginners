#Escribiendo la solucion
precio_helado = 1000
precio_topin = 50
precio_servicio_s = 200

# Pedir al usuario que elija el sabor del waffle
print("Bienvenido. Por favor, elija el sabor de su waffle:")
print("1. Chocolate")
print("2. Vainilla")
print("3. Fresa")

sabor = input("Ingrese el número correspondiente al sabor deseado: ")
while sabor!=1 or sabor!=2 or sabor!=3:
    print("Por favor, seleccione una opción válida.")
    sabor = input("Ingrese el número correspondiente al sabor deseado: ")

if sabor == "1":
    sabor_elegido = "Chocolate"
elif sabor == "2":
    sabor_elegido = "Vainilla"
else:
    sabor_elegido = "Fresa"

# Pedir al usuario que agregue topings
print("¿Desea agregar topings?")
print("1. Sí")
print("2. No")

respuesta_topin = input("Ingrese el número correspondiente a su elección: ")
while respuesta_topin!=1 or respuest_topin!=2:
    print("Por favor, seleccione una opción válida.")
    respuesta_topin = input("Ingrese el número correspondiente a su elección: ")

if respuesta_topin == "1":
    cantidad_topin = int(input("Por favor, indique cuántos topings desea agregar: "))
    total_topin = cantidad_topin * precio_topin
else:
    cantidad_topin = 0
    total_topin = 0

# Pedir al usuario que elija el tipo de servicio
print("¿Desea el waffle para servir o para llevar?")
print("1. Servir")
print("2. Llevar")

tipo_servicio = input("Ingrese el número correspondiente a su elección: ")
while tipo_servicio!=1 or tipo_servicio!=2:
    print("Por favor, seleccione una opción válida.")
    tipo_servicio = input("Ingrese el número correspondiente a su elección: ")

if tipo_servicio == "1":
    tipo_servicio_elegido = "Servir"
    total_servicio = precio_servicio_s
else:
    tipo_servicio_elegido = "Llevar"
    total_servicio = 0

# Calcular el total a pagar
total_a_pagar = precio_helado + total_topin + total_servicio

# Mostrar el total a pagar
print("\nResumen de su orden:")
print(f"Sabor elegido: {sabor_elegido}")
print(f"Cantidad de topings: {cantidad_topin}")
print(f"Tipo de servicio: {tipo_servicio_elegido}")
print(f"Total a pagar: ${total_a_pagar}")

# Solicitar el pago
pago = int(input("\nPor favor, ingrese el monto a pagar: "))

# Calcular el vuelto y mostrarlo
vuelto = pago - total_a_pagar
print(f"Su vuelto es: ${vuelto}")



