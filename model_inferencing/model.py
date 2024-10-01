import requests
from dotenv import load_dotenv
import os

load_dotenv()
LLAMA_URL = os.getenv('LLAMA_URL')

def get_llama_response_v1(input_prompt, system_prompt):
    if not LLAMA_URL:
        raise ValueError("LLAMA_URL is not set in the environment variables.")
    
    headers = {'Content-Type': 'application/json'}
    data = {"input_prompt": input_prompt, "system_message": system_prompt}
    
    try:
        response = requests.post(LLAMA_URL, json=data, headers=headers)
        response.raise_for_status()  
        response_data = response.json()
        
        if 'generated_response' not in response_data or 'generated_text' not in response_data['generated_response']:
            raise ValueError("Unexpected response structure from LLAMA API.")
        
        return response_data['generated_response']['generated_text']
    
    except requests.exceptions.HTTPError as http_err:
        raise SystemError(f"HTTP error occurred: {http_err}") from http_err
    except requests.exceptions.ConnectionError as conn_err:
        raise ConnectionError(f"Error connecting to LLAMA API: {conn_err}") from conn_err
    except requests.exceptions.Timeout as timeout_err:
        raise TimeoutError(f"Request to LLAMA API timed out: {timeout_err}") from timeout_err
    except requests.exceptions.RequestException as req_err:
        raise SystemError(f"An error occurred during the API request: {req_err}") from req_err
    except ValueError as val_err:
        raise ValueError(f"Data error: {val_err}") from val_err
