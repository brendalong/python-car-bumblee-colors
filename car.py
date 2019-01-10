from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, price, ab_count, material="cloth"):
        self.price = price
        self.airbag_count = ab_count
        self.seat_material = material
        super().__init__("car")

    def calc_payments(self, months, rate):
        return f'Your payments for a urchase price of ${self.price} over {months} at {rate} would be too high. Buy something cheaper.'



