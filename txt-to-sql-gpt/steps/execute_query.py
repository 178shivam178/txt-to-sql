import time
from db.execute import execute_query
from prompts.fix_sql_query_prompt import fix_sql_query_error_prompt
import db_schema
from steps.generate_query import generate_sql_query

class QueryExecutionError(Exception):
    """Custom exception for errors in query execution."""
    pass

class QuerySuggestionError(Exception):
    """Custom exception for errors in generating query suggestions."""
    pass

def process_single_query(question, generated_query):
    max_attempts = 3
    attempt = 0

    while attempt < max_attempts:
        try:
            result, error_message = execute_query(generated_query)
            
            if error_message:
                system_prompt = fix_sql_query_error_prompt(
                    question, 
                    result, 
                    error_message, 
                    db_schema.database_schema
                )
    
                print(f"Attempt {attempt + 1} failed: {error_message}")

                try:
                    suggested_query = generate_sql_query(question, system_prompt)
                    if suggested_query:
                        print(f"Received a suggested query from the error resolution API: {suggested_query}")
                        generated_query = suggested_query 
                    else:
                        raise QuerySuggestionError("No suggestions received from the error resolution API.")
                except Exception as e:
                    raise QuerySuggestionError(f"Error generating query suggestion: {str(e)}")
                
                attempt += 1
                time.sleep(1)  
            else:
                print(f"Query executed successfully: {result}")
                return result  

        except Exception as e:
            raise QueryExecutionError(f"An error occurred during query execution: {str(e)}")

    print("All attempts failed. No answer could be obtained for this question.")
    return "No answer could be obtained for this question." 
