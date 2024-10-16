

REQUEST_BODY_JSON = """
{
    "items": [
        {
            "item_id": "string",
            "restaurant_id": "string",
            "order_quantity": 1
        }
    ]
}
"""


RESPONSE_200_JSON = """
{
    "order": {
        "user_id": "string",
        "id": "string",
        "items": [
            {
                "item_id": "string",
                "order_quantity": 1
            }
        ]
    }
}
"""

