distancia_km =int(input("Introduzca la distancia en km")) 
velocidad_kmh =int(input("Introduzca la velocidad en km/h")) 
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")