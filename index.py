from car import Car
from color_picker import ColorPicker


bumblebee = Car(22, 2, "metal")

print("type of vehicle", bumblebee.v_type)

bumblebee_colors = ColorPicker("yellow", interior="black", pinstripe="turquoise")


bumblebee.add_colorscheme(bumblebee_colors)
# or
# bumblebee.add_colorscheme(bumblebee_colors.get_colors())
print(bumblebee.colorscheme.get_colors())