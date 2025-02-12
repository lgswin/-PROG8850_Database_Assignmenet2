import mysql.connector
from mysql.connector import Error

# Database connection details
DB_CONFIG = {
    "host": "localhost",  # Change to your MySQL host
    "user": "root",  # Change to your MySQL username
    "password": "",  # Change to your MySQL password
    "database": "mysql"  # Change to your database name
}

SQL_SCRIPT = """
-- Create the 'projects' table if it does not exist
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);
"""

def execute_sql_script():
    try:
        # Connect to the database
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Execute the table creation script
        for statement in SQL_SCRIPT.strip().split(";"):
            if statement.strip():  # Ensure empty statements are ignored
                cursor.execute(statement)

        # Check if the 'budget' column exists before adding it
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.COLUMNS
            WHERE TABLE_NAME = 'projects' 
            AND COLUMN_NAME = 'budget'
        """)
        column_exists = cursor.fetchone()[0]

        if column_exists == 0:
            cursor.execute("ALTER TABLE projects ADD COLUMN budget DECIMAL(10,2)")
            print("Column 'budget' added successfully.")

        # Commit changes
        connection.commit()
        print("SQL script executed successfully.")

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
    execute_sql_script()