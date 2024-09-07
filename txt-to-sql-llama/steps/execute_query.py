import time
from db.execute import execute_query
from prompts.fix_sql_query_prompt import fix_sql_query_error_prompt
import config
from steps.generate_query import get_llama_response_v1

def process_single_query(question, generated_query):
    max_attempts = 1
    attempt = 0
    result = None
    error_message = None
    while attempt < max_attempts:
        result, error_message = execute_query(generated_query)
        print(result,error_message)
        
        if error_message:
            system_prompt = fix_sql_query_error_prompt(question, 
                                                        result,
                                                        error_message,
                                                        config.database_schema
                                                        )
    
            print(f"Attempt {attempt + 1} failed: {error_message}")
            suggested_query = get_llama_response_v1(question, system_prompt)
            
            if suggested_query:
                print(f"Received a suggested query from the error resolution API: {suggested_query}")
                generated_query = suggested_query 
            else:
                print("No suggestions received from the error resolution API.")
            
            attempt += 1
            time.sleep(1) 
        else:
            print(f"Query executed successfully: {result}")
            return

    print("All attempts failed.")