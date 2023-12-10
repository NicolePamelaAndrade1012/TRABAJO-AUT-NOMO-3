print("Hola Bienvenido a NIRST generador de contraseñas seguras")

def mostrar_menu():
    print("Menú:")
    print("1. Registrar ingreso")
    print("2. Salir")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-2): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Por favor, ingrese un número válido (1-2).")
        except ValueError:
            print("Por favor, ingrese un número entero.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion_elegida = obtener_opcion()

        if opcion_elegida == 1:
            print("Bienvenido al programa de inicio de sesión.")
            break

        elif opcion_elegida == 2:
            print("Fin, espero poder ayudarte en otra ocasión.")
            print("Por favor cierre el programa")

def ingresar_usuario(usuarios):
    intentos_maximos = 100

    for intento in range(intentos_maximos):
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        
        if nombre_usuario in usuarios:
            contrasena = input("Ingrese su contraseña: ")
            if usuarios[nombre_usuario] == contrasena:
                print("¡Inicio de sesión exitoso! Bienvenido, {}.".format(nombre_usuario))
                break
            else:
                print("Contraseña incorrecta. Inténtelo de nuevo.")
        else:
            print("El nombre de usuario no existe. Inténtelo de nuevo.")

        if intento == intentos_maximos - 3:
            print("Demasiados intentos fallidos. Cierre del programa.")
            break

if __name__ == "__main__":
    usuarios_registrados = {
        "María Chávez": "1963",
        "Agustin Andrade": "1957",
        "Nicole Andrade": "1999",
    }
    print("Ingrese su usuario y contraseña.")
    ingresar_usuario(usuarios_registrados)
print("¡¡Listo!!")
print("Comencemos")
print("PROGRAMA GENERADOR DE CONTRASEÑAS")
import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    longitud = int(input("Ingrese la longitud deseada para la contraseña: "))

    if longitud <= 8:
        print("La longitud de la contraseña debe ser mayor que 8.")
        print("Por favor intentelo de nuevo")
    else:
        contrasena_generada = generar_contrasena(longitud)
        print("Contraseña generada: ", contrasena_generada)


print("Fue un gusto ayudarte, gracias por tú visita")