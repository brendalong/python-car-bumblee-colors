class ColorPicker:


# **kwargs - key-word-arguments (makes dictionary) - double ** - could be **other_colors
# *args - arguments (makes list) - single * - could be *colors

    def __init__(self, primary_color, **kwargs):
        self.primary_color = primary_color
        for key, value in kwargs.items():
            # setattr - take all items in dictionary and set as attribute to ColorPicker
            setattr(self, key + "_color", value)

    def get_colors(self):
        # comprehension
        # looking at dictionary k and values (v)
        # for k
        # if 'color' is in the name
        return {k : v for k, v in self.__dict__.items() if 'color' in k}
