from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('API_KEY')
def get_groq_response_generation(prompt):
    try:
        client = Groq(api_key=API_KEY)

        system_prompt = (
            "You are an advanced AI expert skilled in generating questions and SQL queries based on provided database schemas and examples."
        )

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=8192,
            top_p=1,
            stream=False 
        )
        response_content = response.choices[0].message.content 
        return response_content

    except Exception as e:
        error_message = f"API request error: {e}"
        print(error_message)
        return None