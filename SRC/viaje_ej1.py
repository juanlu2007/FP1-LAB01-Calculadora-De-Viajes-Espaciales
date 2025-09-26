distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")
#Esto ocurre ya que el signo "/" realiza la divión completa y "//" hace la división y no continua con el resto y solo muestra el conciente