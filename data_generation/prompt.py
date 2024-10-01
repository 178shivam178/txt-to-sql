def format_prompt_sql_query(db_schema, examples, sample_question, n_number=20):
    example_text = "\n".join(
        [
            f"Question: {example['question']}\nSQL Query: {example['generated_query']}\n"
            for example in examples
        ]
    )
    return f"""
    ### Task
    You are a SQL expert. Your job is to generate data-related question and then generate SQL queries for them accurately for the business team. Refer to the provided database schema for tables and columns for generating the questions as well as the SQL queries. Do not correct spelling mistakes in the schema. 
    The questions should involve complexity based on tables and SQL concepts such as joins, where conditions, and aggregations. We need to generate {n_number} examples.
    do not reapeat same question that I am giving {sample_question} directly think and not copy paste.
    Do not use markdown formatting or any extra text like "Here are five generated questions with their corresponding SQL queries."
    be more creative and think of more questions.

    ## Response
    Format your response as a single list containing multiple dictionaries, where each dictionary has two keys: "generated_question" and "generated_query". Example format:
    
    [
        {{"generated_question": "Your question here", "generated_query": "Your SQL query here"}},
        {{"generated_question": "Another question here", "generated_query": "Another SQL query here"}},
        ...
    ]
    
    ## Sample Questions:
    {sample_question}

    ## Database Schema:
    {db_schema}

    ## Sample Queries:
    {example_text}

    ## Guidelines to follow for generating SQL queries based on generated questions:
    1. Refer to the provided database schema for tables and columns. Do not correct spelling mistakes in the schema.
    2. Your response should only include the SQL queries and nothing else. Do not provide any explanations or additional text. Output only plain text. Do not use markdown formatting or any extra text like "Here are five generated questions with their corresponding SQL queries."
    3. Generate only read/SELECT queries for data safety. If a question cannot be answered using a SELECT operation, it should not be addressed.
    4. Pay close attention to the sample queries to understand how date filters and calculations are performed. Use them as a guide for constructing your SQL query.
    5. Always cast both column and value to lowercase when working with text fields.
    6. Ensure numeric typecasting for numerators in division operations.
    7. Use lowercase for string matching. Typecast to varchar only if needed (mainly in MSSQL).
    8. Apply the same operation in both GROUP BY and SELECT clauses when referencing the same field.
    9. Create aliases for fields in SELECT on which operations are applied.
    10. Prefix field names with table or alias names in joins.
    11. Treat numeric fields as measures and text, enums, and time fields as dimensions in aggregation queries.
    12. Do not refer to the database name in column or table names.
    13. Validate the denominator in division operations to prevent zero division errors.
    14. Exclude null values in aggregations of numeric fields.
    15. Use LOWER in GROUP BY only if the same column in SELECT is also in LOWER.
    16. Consider the granularity of the table and perform appropriate aggregations.
    17. If no time period is mentioned, use data from the last 12 calendar months for calculations unless lifetime value questions are asked.
    19. Order by ABS value where logical.
    20. Round calculations to 2 decimal points, such as AVG and percentages.
    21. Type-cast date columns appropriately for date-based comparisons (if needed).
    """