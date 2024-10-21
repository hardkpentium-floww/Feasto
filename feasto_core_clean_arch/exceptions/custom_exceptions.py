class InvalidRestaurantOwnerId(Exception):
    pass

class InvalidRestaurantId(Exception):
    def __init__(self, restaurant_id):
        self.restaurant_id = restaurant_id

class InvalidUserId(Exception):
    pass

class InvalidItemId(Exception):
    def __init__(self, item_id):
        self.item_id = item_id
