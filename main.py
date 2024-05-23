import os
import sqlite3
import hashlib
import tempfile
import threading

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
    # Hardcoded sensitive information
    secret_key = "12345"  # Ejemplo de información sensible hardcodeada
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

def insecure_sql_query(user_input):
    # Insecure SQL query (SQL Injection vulnerability)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results



def security_vulnerability():
    # Security Vulnerability: Hardcoded credentials
    username = "admin"
    password = "password123"
    print(f"Logging in with username: {username} and password: {password}")

def main():
    # Bug: variable no usada
    unused_variable = "This is not used"
    
    # Bug: posible ruta no válida en diferentes sistemas operativos
    file_path = "/tmp/example.txt"
    db_path = "example.db"
    hardcoded_password = "P@ssw0rd"  # Hardcoded credentials
    api_key = "12345-ABCDE"  # Another hardcoded secret

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

    # Security vulnerability demonstration
    security_vulnerability()

    # Unrestricted eval usage
    eval(user_input)  # This is dangerous and should be avoided

    # Writing to a potentially insecure temporary file
    temp_file_path = "/tmp/tempfile.txt"
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write("This is a temporary file.")
        # Security risk demonstration

    # Insecure SQL query
    results = insecure_sql_query(user_input)
    print(f"SQL Query Results: {results}")

    # Vulnerabilidad: posible inyección de comandos
    os.system(f"echo {user_input}")

    write_file(file_path, user_input)

    # Conexión a una base de datos usando una contraseña hardcodeada
    connection = sqlite3.connect(db_path)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print(f"Connected to the database at {db_path} with password: {HARDCODED_PASSWORD}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

    # Command injection
    os.system(user_input)  # Using user input in system command
    
     
    try:
        write_file(file_path, user_input)
    except Exception as e:
        # Exposing internal errors to the user
        print(f"An error occurred: {e}")  # Improper error handling
    
if __name__ == "__main__":
    main()
