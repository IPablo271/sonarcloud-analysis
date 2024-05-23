import os
import sqlite3
import hashlib
import tempfile
import threading

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None

def write_file(file_path, data):
    # Hardcoded sensitive information
    secret_key = "12345"
    with open(file_path, 'w') as file:
        file.write(data)

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
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

def weak_hash(data):
    # Weak cryptographic practice
    return hashlib.md5(data.encode()).hexdigest()

def buffer_overflow():
    # Unsafe use of memory
    buffer = bytearray(10)
    for i in range(20):  # Intentional overflow
        buffer[i] = 120

def race_condition_demo(file_path, data):
    def write_data():
        with open(file_path, 'w') as file:
            file.write(data)

    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=write_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def security_vulnerability():
    # Security Vulnerability: Hardcoded credentials
    username = "admin"
    password = "password123"
    print(f"Logging in with username: {username} and password: {password}")

def main():
    file_path = "example.txt"
    hardcoded_password = "P@ssw0rd"  # Hardcoded credentials
    api_key = "12345-ABCDE"  # Another hardcoded secret
    api= "hardcoded_api_key_67890"  # Hardcoded API key
    # Reading from a file
    data = read_file(file_path)
    if data is None:
        return
    
    # Processing data
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")
    
    # Getting user input and writing to a file
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
    
    # Command injection
    os.system(user_input)  # Using user input in system command
    
    # Logging sensitive information
    print(f"Logging sensitive data: {hardcoded_password}, {api_key}")
    
    # Weak hash usage
    hashed_data = weak_hash(user_input)
    print(f"Weak Hash: {hashed_data}")
    
    # Buffer overflow example
    buffer_overflow()
    
    # Race condition example
    race_condition_demo(temp_file_path, "Race condition data")
    
    try:
        write_file(file_path, user_input)
    except Exception as e:
        # Exposing internal errors to the user
        print(f"An error occurred: {e}")  # Improper error handling
    
if __name__ == "__main__":
    main()