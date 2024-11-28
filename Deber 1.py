import random

# Función para jugar
def jugar():
    print("\n¡Bienvenido al juego mejorado de adivinanza de números!")
    print("Selecciona un nivel de dificultad:")
    print("1. Fácil (10 intentos, número entre 1 y 50)")
    print("2. Medio (7 intentos, número entre 1 y 100)")
    print("3. Difícil (5 intentos, número entre 1 y 200)")
    
    # Elegir el nivel de dificultad
    nivel = input("Selecciona el nivel (1, 2 o 3): ")
    if nivel == "1":
        intentos_restantes = 10
        numero_secreto = random.randint(1, 50)
    elif nivel == "2":
        intentos_restantes = 7
        numero_secreto = random.randint(1, 100)
    elif nivel == "3":
        intentos_restantes = 5
        numero_secreto = random.randint(1, 200)
    else:
        print("Nivel no válido. Jugando en nivel Medio por defecto.")
        intentos_restantes = 7
        numero_secreto = random.randint(1, 100)

    # Registro de intentos usados
    intentos_usados = 0

    while intentos_restantes > 0:
        try:
            # Solicitar al jugador que adivine
            adivinanza = int(input(f"\nIngresa tu número (Intentos restantes: {intentos_restantes}): "))

            # Comparar la adivinanza con el número secreto
            if adivinanza < numero_secreto:
                print("¡Demasiado bajo! Intenta con un número mayor.")
            elif adivinanza > numero_secreto:
                print("¡Demasiado alto! Intenta con un número menor.")
            else:
                print(f"🎉 ¡Felicidades! Adivinaste el número secreto ({numero_secreto}) correctamente.")
                puntuacion = calcular_puntuacion(intentos_usados, intentos_restantes, nivel)
                registrar_puntuacion(puntuacion)
                break

            intentos_restantes -= 1
            intentos_usados += 1

        except ValueError:
            print("Por favor, ingresa un número válido.")

    if intentos_restantes == 0:
        print(f"😢 Te quedaste sin intentos. El número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")

# Función para calcular la puntuación
def calcular_puntuacion(intentos_usados, intentos_restantes, nivel):
    niveles = {"1": 1, "2": 2, "3": 3}
    puntos_base = niveles.get(nivel, 2) * 100
    puntuacion = puntos_base + (intentos_restantes * 10) - (intentos_usados * 5)
    print(f"Tu puntuación final es: {puntuacion} puntos.")
    return puntuacion

# Función para registrar puntuación
def registrar_puntuacion(puntuacion):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{puntuacion}\n")
    print("Puntuación registrada con éxito.")

# Función para mostrar puntuaciones altas
def mostrar_puntuaciones():
    print("\n=== Puntuaciones Altas ===")
    try:
        with open("puntuaciones.txt", "r") as archivo:
            puntuaciones = archivo.readlines()
            puntuaciones = [int(p.strip()) for p in puntuaciones]
            puntuaciones.sort(reverse=True)
            for i, puntuacion in enumerate(puntuaciones[:5], 1):
                print(f"{i}. {puntuacion} puntos")
    except FileNotFoundError:
        print("No hay puntuaciones registradas todavía.")

# Menú principal
def menu():
    while True:
        print("\n=== Juego Mejorado de Adivinanza de Números ===")
        print("1. Jugar")
        print("2. Ver puntuaciones altas")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_puntuaciones()
        elif opcion == "3":
            print("¡Gracias por jugar! Hasta luego.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Solicitar la ejecucion del programa
menu()
