database_host = "localhost"
username = "root"
password = "178180"
database = "eccomerce"

API = 'https://3c8f-34-41-235-54.ngrok-free.app/v1/llama/response'

database_schema = """{
    "order_values": "This table contains order information aggregated across multiple sources for an e-commerce brand. The table is unique at an Order ID - SKU ID level. The table includes, but is not limited to, all pricing information (like gross sales, tax, net sales, shipping charge, duties, etc.), information related to the product (like SKU, product id/title, price, etc.), order related information (timestamp of order), payment information and shipping information.",
    "marketing_performance": "This table contains detailed marketing performance data for an e-commerce brand, capturing data from various marketing activities and platforms. It provides a comprehensive overview of campaign performance, including spend, clicks, views, impressions, and attributed revenue.",
}

COLUMNS = {
    "order_values": {
        "order_line_item_id": {
            "description": "Unique identifier for each line item in an order",
            "values_sample": ["shopify_5667598663969_14461737632033"],
        },
        "source": {"description": "Source of the order", "values_sample": ["shopify"]},
        "order_id": {
            "description": "Unique identifier for each order",
            "values_sample": ["shopify_5667598663969"],
        },
        "ordered_quantity": {
            "description": "Quantity of each item of a line item",
            "values_sample": [1],
        },
        "tax_percent": {
            "description": "Tax percentage applied to the order",
            "values_sample": [0.17999949556658],
        },
        "total_price_tax": {
            "description": "Total price including tax",
            "values_sample": [152.389468594368],
        },
        "gross_sales_price_before_tax": {
            "description": "Gross sales price before applying tax",
            "values_sample": [846.610531405632],
        },
        "total_discount_after_tax": {
            "description": "Total discount after applying tax",
            "values_sample": [0],
        },
        "total_discount_tax": {
            "description": "Total discount amount subject to tax",
            "values_sample": [0],
        },
        "total_discount_before_tax": {
            "description": "Total discount before applying tax",
            "values_sample": [0],
        },
        "total_returns_before_tax": {
            "description": "Total return/refund amount before tax",
            "values_sample": [846.610531405632],
        },
        "net_sales_before_tax": {
            "description": "Net sales amount before applying tax",
            "values_sample": [0],
        },
        "item_shipping_charge": {
            "description": "Shipping charge for an item",
            "values_sample": [0],
        },
        "item_duties": {
            "description": "Duties charged for an item",
            "values_sample": [0],
        },
        "item_additional_feels": {
            "description": "Additional fees charged for an item",
            "values_sample": [0],
        },
        "total_tax": {"description": "Total tax amount", "values_sample": [0]},
        "total_sales_after_tax": {
            "description": "Total sales amount after applying tax",
            "values_sample": [0],
        },
        "sku_id": {
            "description": "Unique identifier for each stock keeping unit (SKU)",
            "values_sample": ["shopify_8848983261473_47478863036705"],
        },
        "sku_code": {
            "description": "Code assigned to each stock keeping unit (SKU)",
            "values_sample": ["BSL-D-SIP-0001"],
        },
        "product_category": {
            "description": "Category of the product",
            "values_sample": ["Insulated Sipper"],
        },
        "product_id": {
            "description": "Unique identifier for each product",
            "values_sample": ["shopify_8848983261473"],
        },
        "product_title": {
            "description": "Title of the product",
            "values_sample": ["Kids Sipper (430 ml)"],
        },
        "product_price": {
            "description": "Price of the product",
            "values_sample": [999],
        },
        "customer_id": {
            "description": "Unique identifier for each customer",
            "values_sample": ["shopify_7694075199777"],
        },
        "first_ordered_at": {
            "description": "Timestamp of the first order",
            "values_sample": ["2024-02-14 16:00:13.000000"],
        },
        "order_refund_line_item_id": {
            "description": "Unique identifier for each refunded line item in an order",
            "values_sample": ["shopify_5667598663969_14461737632033"],
        },
        "order_date_time": {
            "description": "Date and time of the order",
            "values_sample": ["2024-02-14 16:00:13.000000"],
        },
        "order_date": {
            "description": "Date of the order",
            "values_sample": ["2024-02-14"],
        },
        "order_year": {"description": "Year of the order", "values_sample": [2024]},
        "order_quarter": {
            "description": "Quarter of the year of the order",
            "values_sample": [1],
        },
        "order_month": {"description": "Month of the order", "values_sample": [2]},
        "order_day_of_month": {
            "description": "Day of the month of the order",
            "values_sample": [14],
        },
        "order_week": {
            "description": "Week of the year of the order",
            "values_sample": [7],
        },
        "order_day_of_week": {
            "description": "Day of the week of the order",
            "values_sample": [4],
        },
        "order_hour": {
            "description": "Hour of the day of the order",
            "values_sample": [16],
        },
        "order_minute": {
            "description": "Minute of the hour of the order",
            "values_sample": [0],
        },
        "order_time": {"description": "Time of the order", "values_sample": ["16:00"]},
        "cancellation_status": {
            "description": "Status of order cancellation",
            "values_sample": ["false"],
        },
        "refund_status": {
            "description": "Status of order refund",
            "values_sample": ["false"],
        },
        "order_status": {
            "description": "Status of the order",
            "values_sample": ["unknown"],
        },
        "payment_status": {
            "description": "Status of payment for the order",
            "values_sample": ["pending"],
        },
        "shipping_address_city": {
            "description": "City of the shipping address",
            "values_sample": ["Surat"],
        },
        "shipping_address_state": {
            "description": "State of the shipping address",
            "values_sample": ["Gujarat"],
        },
        "shipping_address_country": {
            "description": "Country of the shipping address",
            "values_sample": ["India"],
        },
    }
}
    "marketing_performance": {
        "marketing_id": {
            "description": "Unique identifier for each marketing activity.",
            "values_sample": [
                "2024-04-01_amazon_sponsored_product_A5IVEQE4ZPVNJ_304143034868101_310419640566194_productAdsamazon_ads_sponsored_products_548576666024459",
                "2024-04-01_amazon_sponsored_product_A5IVEQE4ZPVNJ_405826215303183_448674135385556_productAdsamazon_ads_sponsored_products_511545631860472",
            ],
        },
        "activity_date_time": {
            "description": "Timestamp of the marketing activity.",
            "values_sample": [
                "2024-04-01T00:00:00.000+00:00",
            ],
        },
        "activity_date": {
            "description": "Date of the marketing activity.",
            "values_sample": [
                "2024-04-01T00:00:00.000+00:00",
            ],
        },
        "activity_year": {
            "description": "Year of the marketing activity.",
            "values_sample": ["2024"],
        },
        "activity_quarter": {
            "description": "Quarter of the year in which the marketing activity took place.",
            "values_sample": ["2"],
        },
        "activity_month": {
            "description": "Month of the year in which the marketing activity took place.",
            "values_sample": ["4"],
        },
        "activity_day_of_month": {
            "description": "Day of the month on which the marketing activity took place.",
            "values_sample": ["1"],
        },
        "activity_week": {
            "description": "Week of the year in which the marketing activity took place.",
            "values_sample": ["14"],
        },
        "activity_day_of_week": {
            "description": "Day of the week on which the marketing activity took place (1 for Monday, 7 for Sunday).",
            "values_sample": ["2"],
        },
        "activity_hour": {
            "description": "Hour of the day in which the marketing activity took place.",
            "values_sample": ["0"],
        },
        "activity_minute": {
            "description": "Minute of the hour in which the marketing activity took place.",
            "values_sample": ["0"],
        },
        "activity_time": {
            "description": "Formatted string representation of the marketing activity time.",
            "values_sample": ["00:00"],
        },
        "channel": {
            "description": "Marketing channel used for the activity (e.g., Google Ads, Facebook Ads, Email Marketing).",
            "values_sample": ["sponsored product"],
        },
        "vendor": {
            "description": "Vendor or platform responsible for the marketing activity (e.g., Google, Facebook, Mailchimp).",
            "values_sample": ["amazon"],
        },
        "ad_account_id": {
            "description": "Unique identifier for the ad account associated with the activity.",
            "values_sample": ["A5IVEQE4ZPVNJ"],
        },
        "ad_account_name": {
            "description": "Name of the ad account associated with the activity.",
            "values_sample": ["Famyo"],
        },
        "property_name": {
            "description": "Name of the property or website where the marketing activity was run.",
            "values_sample": ["amazon sponsored product"],
        },
        "network_type": {
            "description": "Type of advertising network used (e.g., Search, Display, Video).",
            "values_sample": ["amazon"],
        },
        "campaign_id": {
            "description": "Unique identifier for the marketing campaign.",
            "values_sample": [
                "304143034868101",
                "405826215303183",
            ],
        },
        "campaign_name": {
            "description": "Name of the marketing campaign.",
            "values_sample": [
                "Football Campaign with presets - B0CT662KJL - 15/2/2024 23:09:44",
                "Hvs_Tar_SP_Blankets_Genric_Mix",
            ],
        },
        "campaign_status": {
            "description": "Current status of the marketing campaign (e.g., Active, Paused, Archived).",
            "values_sample": ["PAUSED", "ENABLED"],
        },
        "adset_id": {
            "description": "Unique identifier for the ad set within the campaign.",
            "values_sample": [
                "310419640566194",
                "448674135385556",
            ],
        },
        "adset_name": {
            "description": "Name of the ad set within the campaign.",
            "values_sample": [
                "Ad group - 15/2/2024 23:09:44",
                "Glow Blankets C1",
            ],
        },
        "adset_status": {
            "description": "Current status of the ad set (e.g., Active, Paused, Archived).",
            "values_sample": ["ENABLED"],
        },
        "ad_id": {
            "description": "Unique identifier for the individual ad within the ad set.",
            "values_sample": [
                "548576666024459",
                "511545631860472",
            ],
        },
        "ad_name": {
            "description": "Name of the individual ad.",
            "values_sample": ["B0CT662KJL", "B0CT6428LV"],
        },
        "ad_description": {
            "description": "Description of the individual ad.",
            "values_sample": [
                "FM_GIDB_Football",
                "FM_GIDB_Astronaut",
            ],
        },
        "ad_status": {
            "description": "Current status of the individual ad (e.g., Active, Paused, Archived).",
            "values_sample": ["ENABLED"],
        },
        "total_spend": {
            "description": "Total amount spent on the marketing activity.",
            "values_sample": ["29.15", "110.15"],
        },
        "total_clicks": {
            "description": "Total number of clicks generated by the marketing activity.",
            "values_sample": ["3", "7"],
        },
        "total_views": {
            "description": "Total number of times the marketing activity was viewed.",
            "values_sample": ["306", "1404"],
        },
        "total_impressions": {
            "description": "Total number of times the marketing activity was displayed.",
            "values_sample": ["0.0"],
        },
        "vendor_reported_orders": {
            "description": "Number of orders attributed to the marketing activity as reported by the marketing vendor.",
            "values_sample": ["0.0"],
        },
        "vendor_reported_revenue": {
            "description": "Revenue generated from orders attributed to the marketing activity as reported by the marketing vendor.",
            "values_sample": ["0.0"],
        },
        "keyword": {
            "description": "Keyword used in the marketing activity (if applicable).",
            "values_sample": [None],
        },
        "_synced_at": {
            "description": "Timestamp indicating when the data was last synced.",
            "values_sample": ["2024-07-16T21:32:08.452+00:00"],
        },
    },
}
"""