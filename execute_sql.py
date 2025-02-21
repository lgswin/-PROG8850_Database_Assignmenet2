import mysql.connector
import os

# Database credentials from GitHub Secrets
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor()
    print("Connected to MySQL Database!")

    # Read and execute SQL files
    sql_files = ["newtable.sql", "add_departments.sql"]  # Add the new SQL script
    for file in sql_files:
        with open(file, "r") as f:
            sql_script = f.read()
            sql_statements = sql_script.split(";")  # Split script by semicolon

            for statement in sql_statements:
                clean_statement = statement.strip()
                if clean_statement:  # Avoid executing empty statements
                    cursor.execute(clean_statement)
                    print(f"Executed: {clean_statement}")

    # Commit changes and close connection
    connection.commit()
    cursor.close()
    connection.close()
    print("SQL execution completed!")

except mysql.connector.Error as err:
    print(f"Error: {err}")