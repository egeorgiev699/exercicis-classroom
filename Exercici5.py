comida = input ("cuanto te ha costado la comida")

IVA = (float(comida) * 0.21)
propina = (float(comida) * 0.1)
total = (float(comida) + (float(propina)) + (float(IVA)))

print ("precio comida = " + str(float( comida)))
print ("IVA = " + str(float(IVA)))
print ("propina = " + str(float(propina)))
print ("total = " + str(float(total)))
