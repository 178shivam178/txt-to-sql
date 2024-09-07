import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

class SQLQueryGenerationError(Exception):
    pass

def generate_sql_query(user_question,system_prompt):
    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7,
            top_p=0.9
        )

        sql_query = response.choices[0].message['content'].strip()
        return sql_query

    except openai.error.OpenAIError as e:
        raise SQLQueryGenerationError(f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise SQLQueryGenerationError(f"An unexpected error occurred: {str(e)}")
