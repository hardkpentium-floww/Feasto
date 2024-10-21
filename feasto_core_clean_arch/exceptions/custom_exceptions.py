class InvalidRestaurantOwnerId(Exception):
    def __init__(self, user_id):
        self.user_id = user_id

class InvalidRestaurantId(Exception):
    def __init__(self, restaurant_id):
        self.restaurant_id = restaurant_id

class InvalidUserId(Exception):
    def __init__(self, user_id):
        self.user_id = user_id

class InvalidItemId(Exception):
    def __init__(self, item_id):
        self.item_id = item_id
