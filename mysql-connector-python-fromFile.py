import mysql.connector
from mysql.connector import Error

# Database connection details
DB_CONFIG = {
    "host": "localhost",  # Change to your MySQL host
    "user": "lgswin",  # Change to your MySQL username
    "password": "Secret5555",  # Change to your MySQL password
    "database": "mysql"  # Change to your database name
}

SQL_FILE_PATH = "newtable.sql"  # Change to the actual path of netable.sql

def execute_sql_file():
    try:
        # Connect to the database
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Read SQL script from file
        with open(SQL_FILE_PATH, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # Split SQL statements and execute each one
        for statement in sql_script.strip().split(";"):
            if statement.strip():  # Ensure empty statements are ignored
                cursor.execute(statement)

        # Commit changes
        connection.commit()
        print("SQL script from file executed successfully.")

    except Error as e:
        print(f"Error executing SQL script: {e}")
        if connection:
            connection.rollback()  # Rollback in case of error

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    execute_sql_file()