sample_example = [
    {
        "question": "Show me trend of sales for the last 6 months",
        "generated_query": """
            SELECT 
                CONCAT(order_year, '-', LPAD(order_month, 2, '0')) AS order_date, 
                SUM(COALESCE(net_sales_before_tax, 0)) AS net_sales 
            FROM 
                order_values 
            WHERE 
                STR_TO_DATE(CONCAT(order_year, '-', LPAD(order_month, 2, '0')), '%Y-%m') >= 
                DATE_FORMAT(CURRENT_DATE - INTERVAL 6 MONTH, '%Y-%m-01') 
                AND STR_TO_DATE(CONCAT(order_year, '-', LPAD(order_month, 2, '0')), '%Y-%m') < 
                DATE_FORMAT(CURRENT_DATE, '%Y-%m-01') 
            GROUP BY 
                order_year, order_month 
            ORDER BY 
                order_year, order_month;

        """
    },
    {
        "question": "Which are the top 5 cities by sales in April 2024?",
        "generated_query": """
            SELECT LOWER(billing_address_city) AS city, 
                   SUM(COALESCE(net_sales_before_tax, 0)) AS total_sales 
            FROM order_values 
            WHERE order_month = 4 AND order_year = 2024 
            AND billing_address_city IS NOT NULL 
            GROUP BY LOWER(billing_address_city) 
            ORDER BY total_sales DESC 
            LIMIT 5;
        """
    }
]
