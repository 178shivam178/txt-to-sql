import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def execute_query(query, params=None):
    connection = None
    result = None
    error_message = None
    
    try:
        with mysql.connector.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                if cursor.with_rows:
                    result = cursor.fetchall()
                connection.commit() 
    except Error as e:
        error_message = str(e)
    finally:
        if connection and connection.is_connected():
            connection.close()
    
    return result, error_message