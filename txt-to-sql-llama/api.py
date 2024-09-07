from prompts.sql_prompt import format_prompt_sql_query
import config as config
from steps.generate_query import get_llama_response_v1
from steps.execute_query import process_single_query

def main():
    database_schema = config.database_schema
    
    user_query = "What was my trend of RTO in last 6 months?"
    
    system_prompt = format_prompt_sql_query(database_schema)
    
    try:
        generated_query = get_llama_response_v1(user_query, system_prompt)
        print(generated_query)
        if generated_query:
            process_single_query(user_query, generated_query)
        else:
            print("No generated query received from LLM model.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
