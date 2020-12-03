botellas0 = input ("cuantas botellas de menos de 1 litro has comprado")
botellas1 = input ("cuantas botellas de mas de 1 litro has comprado")

deposito0 = (0.10*int(botellas0))
deposito1 = (0.25*int(botellas1))

print ("tienes que devolver un total de " + str(float(deposito0) + float(deposito1)) + "centimos")

