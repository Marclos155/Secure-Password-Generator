import random
import string

# Función para generar una contraseña
def generate_password(length=12):
    """
    Genera una contraseña segura con letras, números y caracteres especiales.

    Args:
        length (int): Longitud de la contraseña (por defecto, 12).

    Returns:
        str: Contraseña generada.
    """
    # Combinar letras, números y caracteres especiales
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generar la contraseña seleccionando caracteres al azar
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Pedir la longitud al usuario
if __name__ == "__main__":
    print("Password generator")
    length = int(input("How many caractheres do you want? ") or 12)
    password = generate_password(length)
    print(f"Your password is: {password}")
