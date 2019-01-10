# Base class for creating vehicles of any kind
class Vehicle:

    def __init__(self, v_type="vehicle"):
        self.name = "Vehicle"
        self.v_type = v_type
        self.is_transformed = False

    def add_wheels(self, wheel_num):
        self.wheels = wheel_num

# underscore says that it is private method. Not called directly.
# does not force - just a convention.
    def _add_rockets(self, rocket_num):
        self.rockets = rocket_num

    def transformerize(self, bot_name:str, rocket_num:int):
        self._add_rockets(rocket_num)
        self.wheels = 0
        self.is_transformed = True
        self.bot_name = bot_name

    def add_colorscheme(self, colorsObj):
        self.colorscheme = colorsObj

#if using default, you could leave out by placing _

    def __str__(self):
        return f'This is {self.name}'
