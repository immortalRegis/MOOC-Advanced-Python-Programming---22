# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    
    def bigger(self, compared_to:"RealProperty"):
        return self.square_metres > compared_to.square_metres
    
    def price_difference(self, compared_to:"RealProperty"):
        own_price = self.get_price()
        other_price = compared_to.get_price()

        return abs(own_price - other_price)
    
    def get_price(self):
        return self.square_metres * self.price_per_sqm

    def more_expensive(self, compared_to:"RealProperty"):
        own_price = self.get_price()
        other_price = compared_to.get_price()

        return own_price > other_price
