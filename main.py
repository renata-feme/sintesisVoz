import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[32].id)

nombre = input("¿Cuál es tu nombre? ")

saludo = f"Hola, {nombre}! Gracias por usar el lector de texto!"
print(saludo)
print("En caso de querer detener el progama, puede escribir parar")
print("En caso de querer salir del progama, puede escribir salir")
engine.say(saludo)
engine.runAndWait()

while True:
    texto = input("\nEscribe el texto que quieres convertir a voz: ")

    if texto == "Parar" or "parar":
        print("Se ha detenido la voz a petición del usuario.")
        engine.stop()
        continue

    if texto == "Salir" or "salir":
        print("Saliendo del programa")
        adios = f"Gracias, {nombre}, por usar el lector de texto, adiós!"
        print(adios)
        engine.say(adios)
        engine.runAndWait()
        break

    engine.say(texto)
    engine.runAndWait()
