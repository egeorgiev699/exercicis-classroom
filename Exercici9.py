def calcula_preu_total(menjar):

    IVA = round((float(menjar) * 0.1),2)
    Propina = round((float(menjar) * 0.1),2)
    Preu_total = round((float(menjar) + float(IVA) + float(Propina)),2)

    print("\nPreu del menjar: " + str(float(menjar)))
    print("IVA: " + str(float(IVA)))
    print("Propina: " + str(float(Propina)))
    print("Preu total: " + str(float(Preu_total))+ "\n")

    return Preu_total


num_personas = int(input("Quantes persones sou? "))


preu_total = 0
for i in range(num_personas):

    print("Tria el plat")
    print("1- Pizza 6€")
    print("2- Ensalada 4€")
    print("3- Kebab 3€")
    print("4- Salmó 8€")

    num_ordre = int(input("\n Escriu el número del plat: "))

    if num_ordre == 1:
        preu_plat = calcula_preu_total(6)
    elif num_ordre == 2:
        preu_plat = calcula_preu_total(4)

    elif num_ordre == 3:
        preu_plat = calcula_preu_total(3)
    elif num_ordre == 4:
        preu_plat = calcula_preu_total(8)
    else:
        print("El plat que has elegit no esta disponible.")
        preu_plat = 0

    preu_total = preu_total + preu_plat

print("El preu total és " + str(round(preu_total,2)) + "€")