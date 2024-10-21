

REQUEST_BODY_JSON = """
{
    "items": [
        {
            "item_id": 1,
            "restaurant_id": 1,
            "order_quantity": 1
        }
    ]
}
"""


RESPONSE_200_JSON = """
{
    "order": {
        "user_id": "string",
        "id": 1,
        "created_at": "2099-12-31 00:00:00",
        "updated_at": "2099-12-31 00:00:00",
        "items": [
            {
                "item_id": 1,
                "order_quantity": 1
            }
        ]
    }
}
"""

