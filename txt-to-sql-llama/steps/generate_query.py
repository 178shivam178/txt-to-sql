import requests
import config
import os

def get_llama_response_v1(input_prompt,system_prompt):
    """Send the prompt to the LLM model and return the response."""
    api_url = os.getenv('LLM_API_URL',config.API )
    headers = {'Content-Type': 'application/json'}
    data = {"input_prompt": input_prompt,"system_prompt":system_prompt}
    
    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        return response_data.get('generated_query')
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None