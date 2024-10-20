import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",  # Update with your MySQL server host
            user="your_username",  # Update with your MySQL username
            password="your_password"  # Update with your MySQL password
        )
        cursor = conn.cursor()

        # SQL to create the database if it doesn't already exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute the query
        cursor.execute(create_db_query)
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle different types of errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")

    finally:
        # Close cursor and connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

