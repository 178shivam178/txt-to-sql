database_info = """
TABLE_DESCRIPTIONS = {
    "order_values": "This table contains order information aggregated across multiple sources for an e-commerce brand. The table is unique at an Order ID - SKU ID level. The table includes, but is not limited to, all pricing information (like gross sales, tax, net sales, shipping charge, duties, etc.), information related to the product (like SKU, product id/title, price, etc.), order related information (timestamp of order), payment information and shipping information."
}
COLUMNS = {
    "order_values": {
        "order_line_item_id": {
            "description": "Unique identifier for each line item in an order",
            "values_sample": ["amazon_10018509881995"],
        },
        "source": {
            "description": "Channel the order was placed on",
            "values_sample": ["amazon"],
        },
        "order_id": {
            "description": "Unique identifier for each order",
            "values_sample": ["amazon_406-3422484-3053949"],
        },
        "ordered_quantity": {
            "description": "Quantity of each item of a line item",
            "values_sample": [1],
        },
        "gross_sales_price_after_tax": {
            "description": "Gross sales for the line item after tax",
            "values_sample": [399],
        },
        "tax_percent": {
            "description": "Tax percentage applied to the order",
            "values_sample": [0.17999887],
        },
        "total_price_tax": {
            "description": "Total tax amount applied to the price",
            "values_sample": [60.86],
        },
        "gross_sales_price_before_tax": {
            "description": "Gross sales for the line item before tax",
            "values_sample": [338.14],
        },
        "total_discount_after_tax": {
            "description": "Total discount applied after tax",
            "values_sample": [0],
        },
        "total_discount_tax": {
            "description": "Total discount tax amount",
            "values_sample": [0],
        },
        "total_discount_before_tax": {
            "description": "Total discount applied before tax",
            "values_sample": [0],
        },
        "total_cancellation_returns_before_tax": {
            "description": "Amount of cancelled orders before tax",
            "values_sample": [0],
        },
        "total_rto_returns_before_tax": {
            "description": "Amount of RTO (Return to Origin) orders before tax",
            "values_sample": [0],
        },
        "total_returns_refund_before_tax": {
            "description": "Amount of returned orders excluding RTO before tax",
            "values_sample": [0],
        },
        "total_returns_before_tax": {
            "description": "Total amount of returned orders including RTO before tax",
            "values_sample": [0],
        },
        "total_return_tax": {
            "description": "Total tax amount on returns",
            "values_sample": [0],
        },
        "net_sales_before_tax": {
            "description": "Net sales amount before applying tax",
            "values_sample": [338.14],
        },
        "item_shipping_charge": {
            "description": "Shipping income/revenue collected from the customer for an item",
            "values_sample": [0],
        },
        "item_duties": {
            "description": "Duties collected from the customer for an item",
            "values_sample": [0],
        },
        "item_additional_fees": {
            "description": "Additional fees collected from the customer for an item",
            "values_sample": [0],
        },
        "total_tax": {
            "description": "Total tax amount",
            "values_sample": [60.86],
        },
        "total_sales_after_tax": {
            "description": "Total sales amount after applying tax",
            "values_sample": [399],
        },
        "gross_merchandise_value": {
            "description": "Gross Merchandise Value (GMV) for an item",
            "values_sample": [399],
        },
        "sku_id": {
            "description": "Unique identifier for each stock keeping unit (SKU)",
            "values_sample": ["amazon_B09XTXHBJQ"],
        },
        "sku_code": {
            "description": "Code assigned to each stock keeping unit (SKU)",
            "values_sample": ["B09XTXHBJQ"],
        },
        "product_category": {
            "description": "Category of the product",
            "values_sample": ["Wings Crosshair 200 Wired Optical Gaming Mouse (USB 3.0, Black), one Size (WL-CROSSHAIR200-BLK)"],
        },
        "product_id": {
            "description": "Unique identifier for each product",
            "values_sample": ["B09XTXHBJQ"],
        },
        "product_title": {
            "description": "Title of the product",
            "values_sample": ["Wings Crosshair 200 Wired Optical Gaming Mouse (USB 3.0, Black), one Size (WL-CROSSHAIR200-BLK)"],
        },
        "product_price": {
            "description": "Price of the product",
            "values_sample": [338.14],
        },
        "customer_id": {
            "description": "Unique identifier for each customer",
            "values_sample": ["zrfjhy0c5mrcgrj@marketplace.amazon.in"],
        },
        "first_ordered_at": {
            "description": "Timestamp of the first order",
            "values_sample": ["2022-12-29 15:24:48"],
        },
        "order_refund_line_item_id": {
            "description": "Unique identifier for each refunded line item in an order",
            "values_sample": ["amazon_10018509881995"],
        },
        "order_date_time_utc": {
            "description": "UTC date and time of the order",
            "values_sample": ["2022-12-29 9:54:48"],
        },
        "order_date_time": {
            "description": "Date and time of the order",
            "values_sample": ["2022-12-29 15:24:48"],
        },
        "order_date": {
            "description": "Date of the order",
            "values_sample": ["2022-12-29"],
        },
        "order_year": {
            "description": "Year of the order",
            "values_sample": [2022],
        },
        "order_quarter": {
            "description": "Quarter of the year of the order",
            "values_sample": [4],
        },
        "order_month": {
            "description": "Month of the order",
            "values_sample": [12],
        },
        "order_day_of_month": {
            "description": "Day of the month of the order",
            "values_sample": [29],
        },
        "order_week": {
            "description": "Week of the year of the order",
            "values_sample": [52],
        },
        "order_day_of_week": {
            "description": "Day of the week of the order",
            "values_sample": [5],
        },
        "order_hour": {
            "description": "Hour of the day of the order",
            "values_sample": [15],
        },
        "order_minute": {
            "description": "Minute of the hour of the order",
            "values_sample": [24],
        },
        "order_time": {
            "description": "Time of the order",
            "values_sample": ["15:24"],
        },
        "refund_status": {
            "description": "Status of order refund",
            "values_sample": ["FALSE"],
        },
        "rto_status": {
            "description": "Status of RTO for the order",
            "values_sample": ["FALSE"],
        },
        "cancellation_status": {
            "description": "Status of order cancellation",
            "values_sample": ["FALSE"],
        },
        "order_status": {
            "description": "Status of the order",
            "values_sample": ["fulfilled"],
        },
        "payment_status": {
            "description": "Status of payment for the order",
            "values_sample": ["paid"],
        },
        "return_reason": {
            "description": "Reason for return if applicable",
            "values_sample": [""],
        },
        "billing_address_city": {
            "description": "City in the customer address",
            "values_sample": ["HATHRAS"],
        },
        "billing_address_state": {
            "description": "State in the customer address",
            "values_sample": ["UTTAR PRADESH"],
        },
        "billing_address_country": {
            "description": "Country in the customer address",
            "values_sample": ["India"],
        },
        "gift_wrap_expense": {
            "description": "Expenses associated with gift wrapping",
            "values_sample": [0],
        },
        "packaging_expense": {
            "description": "Expenses associated with packaging of goods",
            "values_sample": [0],
        },
        "handling_expense": {
            "description": "Expenses associated with handling of goods",
            "values_sample": [0],
        },
        "shipping_expense": {
            "description": "Shipping/logistics expense for the items",
            "values_sample": [29.89468],
        },
        "marketplace_expense": {
            "description": "Fees paid to the marketplace like Amazon/Flipkart",
            "values_sample": [77.44643],
        },
        "payment_gateway_expense": {
            "description": "Fees paid to the payment gateway",
            "values_sample": [0],
        },
        "other_adjustments": {
            "description": "Any other financial adjustments",
            "values_sample": [0],
        },
        "estimated_expense": {
            "description": "Estimated expenses associated with the order",
            "values_sample": [0],
        },
        "sku_cost": {
            "description": "Cost of the SKU",
            "values_sample": [0],
        },
        "gross_profit": {
            "description": "Gross profit from the order",
            "values_sample": [338.14],
        },
        "cm1_expense": {
            "description": "Expense related to CM1 (Contribution Margin 1)",
            "values_sample": [107.34111],
        },
        "profit_cm1": {
            "description": "Contribution Margin 1 profit",
            "values_sample": [230.7989],
        },
        "_synced_at": {
            "description": "Timestamp when the data was last synced",
            "values_sample": ["2024-08-22 22:57:21"],
        },
    }
}
"""