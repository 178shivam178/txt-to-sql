from config.db_schema import database_info
from config.examples import sample_example
from data_generation.prompt import format_prompt_sql_query
from data_generation.model import get_groq_response_generation

def generate_question_query(question):
    try:
        print(f"Processing question: {question}")
        
        input_prompt = format_prompt_sql_query(database_info, sample_example, question, n_number=25)
        generated_response = get_groq_response_generation(input_prompt)
        return question, generated_response
    
    except Exception as e:
        print(f"Error processing the question: {e}")
        return question, f"Error: {e}"

question = "How many countries are in North America?"
result = generate_question_query(question)
print(result)
print(type(result))