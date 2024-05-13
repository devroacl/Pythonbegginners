
puntaje_final_total = 0
respuestas_correctas_total = 0
respuestas_incorrectas_total = 0
respuestas_en_blanco_total = 0

numero_postulantes = int(input("Ingrese el número de postulantes: "))

for i in range(1, numero_postulantes + 1):
    try:
        respuestas_correctas = int(input(f"Ingrese el número de respuestas correctas para el postulante {i}: "))
        respuestas_incorrectas = int(input(f"Ingrese el número de respuestas incorrectas para el postulante {i}: "))
        respuestas_en_blanco = int(input(f"Ingrese el número de respuestas en blanco para el postulante {i}: "))
        
        if respuestas_correctas < 0 or respuestas_incorrectas < 0 or respuestas_en_blanco < 0:
            print("Las respuestas no pueden ser negativas.")
            continue  # Salta a la siguiente iteración del bucle
        
        puntaje_final = (respuestas_correctas * 3) + (respuestas_incorrectas * -1) + (respuestas_en_blanco * 0)
        
        puntaje_final_total += puntaje_final
        respuestas_correctas_total += respuestas_correctas
        respuestas_incorrectas_total += respuestas_incorrectas
        respuestas_en_blanco_total += respuestas_en_blanco

        print(f"Puntaje final del postulante {i}: {puntaje_final}")
    
    except ValueError:
        print("Por favor, ingrese un número válido.")

puntaje_total_maxposible = (respuestas_correctas_total * 3) + (respuestas_incorrectas_total * -1)

print(f"Puntaje total posible: {puntaje_total_maxposible}")
print(f"Puntaje final total de todos los postulantes: {puntaje_final_total}")
print(f"Respuestas correctas totales: {respuestas_correctas_total}")
print(f"Respuestas incorrectas totales: {respuestas_incorrectas_total}")
print(f"Respuestas en blanco totales: {respuestas_en_blanco_total}")
