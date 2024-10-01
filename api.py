from flask import Flask, request, jsonify, render_template
from config.db_schema import database_info
from model_inferencing.prompt import format_prompt_sql_query
from model_inferencing.model import get_llama_response_v1
from sql_execution.execute import process_single_query

app = Flask(__name__)

def model_main(question):
    try:
        system_prompt = format_prompt_sql_query(database_info)
        generated_query = get_llama_response_v1(question, system_prompt)
        status, result, generated_query = process_single_query(question, generated_query)
        
        return {
            "question": question,
            "generated_query": generated_query,
            "status": status,
            "response": result 
        }
    except Exception as e:
        app.logger.error(f"Error processing question: {str(e)}")
        
        return {
            "question": question,
            "generated_query": None,
            "status": "error",
            "response": f"An error occurred: {str(e)}"
        }

@app.route("/generate_query", methods=["POST"])
def generate_query():
    try:
        data = request.get_json()
        question = data.get("question", "")
        if question:
            response = model_main(question)
            return jsonify(response)
        return jsonify({"error": "No question provided"}), 400
    except Exception as e:
        app.logger.error(f"Error in generate_query endpoint: {str(e)}")
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3008,debug=True)
