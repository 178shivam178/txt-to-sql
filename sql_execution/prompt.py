def fix_sql_query_error_prompt(question, sql_query, error, database_schema):
    return f"""
    Review the following SQL query and the associated error. Provide the corrected version of the SQL query. If the query is correct, return it without modifications. Do not provide any explanations or additional text.

    Question:
    {question}

    SQL Query with Error:
    {sql_query}

    Error Message:
    {error}

    Ensure the SQL query matches the exact table names and column names specified in the following schema: {database_schema}.

    Format your response as JSON, including only the SQL query in the following format:

    Your SQL Query Here
    """
