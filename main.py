import os
import sqlite3

# Ejemplo de contraseña hardcodeada (mala práctica)
HARDCODED_PASSWORD = "password123"

def read_file(file_path):
    try:
        # Vulnerabilidad: No manejo de paths absolutos
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    except Exception as e:
        # Error: Capturar excepciones genéricas
        print(f"An error occurred: {e}")
        return None

def write_file(file_path, data):
    # Vulnerabilidad: datos del usuario se escriben sin sanitización
    with open(file_path, 'w') as file:
        file.write(data)
    print("Data written to file successfully")

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    # Error: Posible fallo si data es None
    if data is None:
        return None
    processed_data = data.lower()
    return processed_data

def connect_to_database(db_path, password):
    # Simulación de conexión a una base de datos usando una contraseña hardcodeada
    if password != HARDCODED_PASSWORD:
        print("Incorrect password.")
        return None
    try:
        connection = sqlite3.connect(db_path)
        print(f"Connected to the database at {db_path} with password: {password}")
        return connection
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Bug: variable no usada
    unused_variable = "This is not used"
    
    # Bug: posible ruta no válida en diferentes sistemas operativos
    file_path = "/tmp/example.txt"
    db_path = "example.db"
    
    # Lectura de un archivo
    data = read_file(file_path)
    if data is None:
        return
    
    # Procesamiento de datos
    processed_data = process_data(data)
    if processed_data is None:
        print("No data to process.")
        return
    print(f"Processed Data: {processed_data}")
    
    # Obtener entrada del usuario y escribir en un archivo
    user_input = get_user_input()
    
    # Vulnerabilidad: posible inyección de comandos
    os.system(f"echo {user_input}")
    
    write_file(file_path, user_input)

    # Uso de una contraseña hardcodeada para conectar a la base de datos
    connection = connect_to_database(db_path, HARDCODED_PASSWORD)
    if connection:
        connection.close()

if __name__ == "__main__":
    main()
