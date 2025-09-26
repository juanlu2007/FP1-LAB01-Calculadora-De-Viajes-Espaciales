distancia=int(input("Intoduzca la distancia en km"))
paradas=0
for i in range(15000,distancia,15000):
    print(f"Parada en el km {i}")
    paradas= paradas+1
print(f"Total de paradas para respostar: {paradas}")

