def obtenir_vocals(frase):
    vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    num_vocals = 0

    for lletra in frase:
        if  lletra in vocals:
            num_vocals = num_vocals + 1

    print(num_vocals)

frase = input("Escriu una frase aleatòria")

obtenir_vocals(frase)
