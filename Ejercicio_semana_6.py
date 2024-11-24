intentos = 0  # Contador de intentos fallidos

while intentos < 3:
    # Solicitar la contraseña
    contraseña = input("Ingrese una contraseña: ")

    # Verificar si la contraseña comienza con un número
    if not contraseña[0].isdigit():
        print("La contraseña debe comenzar con un número.")
        intentos += 1
        continue

    # Solicitar la confirmación de la contraseña
    confirmacion = input("Ingrese la contraseña nuevamente: ")

    # Verificar si coinciden
    if contraseña == confirmacion:
        print("Contraseña correcta")
        print("Fin del programa")
        break
    else:
        print("Las contraseñas no coinciden.")
        intentos += 1

# Si el usuario falla 3 veces
if intentos == 3:
    print("Se han cometido demasiados errores.")
    print("Fin del programa")
