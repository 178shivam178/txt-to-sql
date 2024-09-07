import mysql.connector
from mysql.connector import Error
import config

def execute_query(query):
    connection = None
    error_message = None
    try:
        connection = mysql.connector.connect(
            host=config.database_host,
            user=config.username,
            password=config.password,
            database=config.database
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result, None  
    except Error as e:
        error_message = str(e)  
        return None, error_message
    finally:
        if connection and connection.is_connected():
            connection.close()