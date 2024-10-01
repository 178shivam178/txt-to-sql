import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import time
from config.db_schema import database_info
from sql_execution.prompt import fix_sql_query_error_prompt
from sql_execution.model import get_groq_response_v2

load_dotenv()

def execute_query(query):
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            cursor.close()
            connection.close()
            return 'Success', result

    except Error as e:
        raise e  
        return 'Failed', str(e)

def process_single_query(question, generated_query):
    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        try:
            status, result = execute_query(generated_query)
            if status == 'Success':
                return status, result, generated_query
        except Error as e:
            raise e
            return 'Failed', str(e)

        system_prompt = fix_sql_query_error_prompt(question, generated_query, result, database_info)
        suggested_query = get_groq_response_v2(system_prompt)

        if suggested_query:
            generated_query = suggested_query
        else:
            return 'Failed', "No suggestions received from the error resolution API.", generated_query
        
        attempt += 1
        time.sleep(1)  
    
    return 'Failed', "All attempts failed.", generated_query
