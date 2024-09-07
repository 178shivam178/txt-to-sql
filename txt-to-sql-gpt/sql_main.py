from prompts.sql_prompt import format_prompt_sql_query
import db_schema as db_schema
from steps.generate_query import generate_sql_query
from steps.execute_query import process_single_query

def execute_user_query(user_query):
 
    database_schema = db_schema.database_schema
    
    system_prompt = format_prompt_sql_query(database_schema)
    
    try:
        generated_query = generate_sql_query(user_query, system_prompt)
        
        if not generated_query:
            return "No generated query received from the LLM model."
        
        result = process_single_query(user_query,generated_query)
        
        return result
        
    except ConnectionError:
        return "Database connection error. Please check your connection settings."
    except SyntaxError:
        return "Error in the generated SQL query syntax."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

