import mysql.connector
import os

# GitHub Secrets
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_ADMIN_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# MySQL connection
try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor()
    print("Connected to MySQL Database!")

    # run SQL file
    sql_files = ["newtable.sql"] 
    for file in sql_files:
        with open(file, "r") as f:
            sql_script = f.read()
            cursor.execute(sql_script, multi=True)
            print(f"Executed {file} successfully.")

    connection.commit()
    cursor.close()
    connection.close()
    print("SQL execution completed!")

except mysql.connector.Error as err:
    print(f"Error: {err}")