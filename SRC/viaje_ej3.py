
edad=int(input("Introduza su edad"))
lv_fisico=int(input("introduzca su nivel fisico (1-10)"))
while lv_fisico>10 or lv_fisico<1:
    lv_fisico=int(input("introduzca su nivel fisico (1-10)"))
if edad<18:
    print("Debe ser mayor de edad para embarcarse")
elif lv_fisico<5:
     print("Debe mejorar su forma fisica")
else:
    print("¡Listo para despegar!")