# Definimos el número secreto
numero_secreto = 7

# Esta variable controlará si el juego continúa activo
adivinado = False

print("--- ¡BIENVENIDO AL JUEGO DEL NÚMERO SECRETO! ---")

# MIENTRAS 'adivinado' sea falso, el código de adentro se repetirá
while not adivinado:
    intento = int(input("Adivina el número secreto (del 1 al 10): "))
    
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        adivinado = True  # Esto rompe el bucle y termina el programa
    elif intento > numero_secreto:
        print("Casi, pero tu número es muy alto. ¡Intenta de nuevo!\n")
    else:
        print("Casi, pero tu número es muy bajo. ¡Intenta de nuevo!\n")

print("Gracias por jugar.")