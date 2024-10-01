from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_groq_response_v2(prompt):
    if not API_KEY:
        raise ValueError("API_KEY is not set in the environment variables.")
    
    client = Groq(api_key=API_KEY)
    
    system_prompt = (
        "You are an advanced AI expert skilled in fixing errors for SQL queries."
    )

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False
        )
        response_content = response.choices[0].message.content
        return response_content

    except Exception as e:
        error_message = f"API request error: {e}"
        raise RuntimeError(error_message) from e 
