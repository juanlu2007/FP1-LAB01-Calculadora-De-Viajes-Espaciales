semanas=0
dias=0
for i in range(10000,60000,10000):
    tiempo=(225000000/i)/24
    semanas=tiempo//7
    dias=tiempo%7

    print(f"Velocidad: {i}Km/h -> Tiempo: {semanas} semanas y {dias} dias")
